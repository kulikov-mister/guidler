# handlers/user/add_instruction.py
import asyncio
from sqlalchemy.exc import IntegrityError
from main import logging

from aiogram import Router, F
from aiogram.types import (
    Message, CallbackQuery, ChatMemberUpdated, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
)
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from Filter.Filter import IsNotCommand, is_valid_language_code
from database.add_to_db import add_instruction
from database.get_to_db import get_user, check_instruction, get_user_instructions, get_user_unique_chats, get_instructions_by_group_id
from keyboards.reply.admin_request import get_add_bot_to_group_keyboard
from keyboards.inline.user_inline.approve_channel import keyboard_approve_channel
from loader import dp, bot
from lang.get_message import get_message, extract_language
from states.user_states import CreateInstruction
from config_data.config import ADMIN_IDS
from utils.cache_utils import CacheManager
from utils.code_generator import generate_random_string_async, generate_random_string_async_lower
from utils.imgur_downloader import upload_image
from config_data.config import BOT_TOKEN

router = Router()
dp.include_router(router)
cache_manager = CacheManager()


# команда add_instruction
@router.message(Command('add_instruction'))
async def add_instruction_command(message: Message, state: FSMContext):
    lang = extract_language(message)
    user_id = message.from_user.id
    message_id = message.message_id
    user_data = await get_user(user_id)
    if user_data is None:
        await message.answer(get_message(lang, "registration_required_message"))
        return

    instruction_msg = get_message(lang, "choose_channel_message")
    instructions = await get_user_instructions(user_id)

    await message.answer(get_message(lang, "micro_plan_add_instruction"))
    await asyncio.sleep(2)

    r = 2 if instructions else 1
    code = await generate_random_string_async()
    inline_kb = get_add_bot_to_group_keyboard(lang, str(user_id), code, r)
    await message.answer(instruction_msg, reply_markup=inline_kb)
    await state.update_data(message_id=message_id+1, code=code)
    await state.set_state(CreateInstruction.GroupId)


# проверка на добавление бота админом в канал или группу
@router.my_chat_member(CreateInstruction.GroupId)
async def on_chat_member_join(update: ChatMemberUpdated, state: FSMContext):
    lang = extract_language(update)
    status = update.new_chat_member.status
    user_id = str(update.from_user.id)  # ID пользователя, который добавил бота
    group_id = update.chat.id  # ID группы или канала
    group_name = update.chat.full_name  # Название группы или канала
    state_data = await state.get_data()
    message_id = int(state_data.get('message_id'))+1 if state_data else None

    if status == "administrator":

        chat_member = await bot.get_chat_member(chat_id=group_id, user_id=bot.id)
        if chat_member.can_post_messages and chat_member.can_edit_messages and chat_member.can_delete_messages:

            chat_info = await bot.get_chat(chat_id=group_id)
            if chat_info.photo:
                # Получаем file_id аватара чата
                photo_file_id = chat_info.photo.big_file_id
                file = await bot.get_file(photo_file_id)
                file_path = file.file_path
                file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
                image_url = upload_image(file_url)

            else:
                image_url = "https://i.imgur.com/Dnm3RRZ.png"
            msg = get_message(lang, "sent_name_instruction")
            await state.update_data(group_id=group_id, group_name=group_name, image_url=image_url)
            await state.set_state(CreateInstruction.Name)
            await bot.edit_message_text(msg, user_id, message_id, reply_markup=None)

        else:
            # Бот не обладает всеми необходимыми правами администратора
            msg = get_message(lang, "no_rights_in_channel")
            await bot.edit_message_text(msg, user_id, message_id, reply_markup=None)


# инлайн режим для поиска чатов пользователя с капчей
@router.inline_query(F.query.startswith('#ch'), CreateInstruction.GroupId)
async def query_choose_chat(inline_query: InlineQuery, state: FSMContext):
    lang = extract_language(inline_query)
    user_id = inline_query.from_user.id
    state_data = await state.get_data()
    code = state_data.get('code')
    query_code = inline_query.query[3:]
    results = []

    # прохождение капчи от частых запросов и ботов
    if query_code == code:
        # Получаем уникальные чаты пользователя
        unique_chats = await get_user_unique_chats(user_id)

        for group_id, (group_name, instruction_title, image_url) in unique_chats.items():
            # Создаем результат для каждого чата
            results.append(
                InlineQueryResultArticle(
                    id=group_id,
                    title=group_name,
                    description=get_message(
                        lang, "your_channel_name")+instruction_title,
                    thumbnail_url=image_url or "https://i.imgur.com/Dnm3RRZ.png",
                    input_message_content=InputTextMessageContent(
                        message_text=get_message(
                            lang, "inline_chat_selection", group_name=group_name, group_id=group_id)
                    ),
                    reply_markup=keyboard_approve_channel(
                        lang, group_id, group_name)
                )
            )
        # Отправляем результаты обратно пользователю
        await inline_query.answer(
            results=results, cache_time=0,
            switch_pm_text=get_message(lang, "switch_pm_text"),
            switch_pm_parameter="long",
        )

    elif query_code != code:
        # обнуление капчи
        description = get_message(lang, "code_404_description")
        results.append(
            InlineQueryResultArticle(
                id="1",
                title=get_message(lang, "code_404"),
                description=description,
                thumbnail_url="https://sun6-22.userapi.com/s/v1/if1/rLwx4UQ-0gPXldP0i_OLqIA4GwU6qcv9F4Nq0DxgG_gPp5goeEQtIIfLUfvAri67tAGHiqhX.jpg?size=250x250&quality=96&crop=0,0,250,250&ava=1",
                input_message_content=InputTextMessageContent(
                    message_text=f"<b>{description}</b>"
                )
            )
        )
        await inline_query.answer(
            results=results,
            cache_time=0,
            switch_pm_text=get_message(lang, "switch_pm_text"),
            switch_pm_parameter="short",
        )
        await state.update_data(code=None)


# колбек для подтверждения выбора категории
@router.callback_query(F.data.startswith('#ch_'), CreateInstruction.GroupId)
async def handle_chat_selection_callback(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    _, group_id, group_name = call.data.split('_')

    chat_member = await bot.get_chat_member(chat_id=group_id, user_id=bot.id)
    if chat_member.status not in ["administrator", "creator"]:
        msg = get_message(lang, "bot_not_admin_message")
        await call.answer(msg, show_alert=True)
        return

    if chat_member.can_post_messages and chat_member.can_edit_messages and chat_member.can_delete_messages:
        chat_info = await bot.get_chat(chat_id=group_id)
        if chat_info.photo:
            # Получаем file_id аватара группы или канала
            photo_file_id = chat_info.photo.big_file_id
            file = await bot.get_file(photo_file_id)
            file_path = file.file_path
            file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
            image_url = upload_image(file_url)
        else:
            image_url = "https://i.imgur.com/Dnm3RRZ.png"

        await state.update_data(group_id=group_id, group_name=group_name, image_url=image_url)
        await call.answer(get_message(lang, "channel_approved"))
        await bot.edit_message_text(inline_message_id=call.inline_message_id, text=get_message(lang, "channel_approved"), reply_markup=None)
        await bot.send_message(call.from_user.id, get_message(lang, "sent_name_instruction"))
        await state.set_state(CreateInstruction.Name)

    else:
        # Бот не обладает всеми необходимыми правами администратора
        msg = get_message(lang, "no_rights_in_channel")
        await call.answer(msg, show_alert=True)


# проверка на удаление бота из канала или группы
@router.my_chat_member()
async def on_chat_member_update(update: ChatMemberUpdated):
    lang = extract_language(update)
    if update.new_chat_member.status in ["left", "kicked"]:
        group_id = update.chat.id

        # Получаем инструкции, связанные с этой группой/каналом
        instructions = await get_instructions_by_group_id(group_id)
        if instructions:
            admin_instructions = {}  # Словарь для хранения инструкций по admin_user_id

            for instruction in instructions:
                admin_user_id = instruction.user_id  # ID пользователя, создавшего инструкцию
                if admin_user_id not in admin_instructions:
                    admin_instructions[admin_user_id] = []
                admin_instructions[admin_user_id].append(instruction.title)

            for admin_user_id, titles in admin_instructions.items():
                message_text = get_message(lang, "canal_kicked_msg")
                for title in titles:
                    message_text += f"\n- {title}"

                try:
                    # Отправляем уведомление каждому администратору со списком его инструкций
                    await bot.send_message(admin_user_id, message_text)
                except Exception as e:
                    print(
                        f"Ошибка при отправке сообщения пользователю {admin_user_id}: {e}")


# добавление инструкции
@router.message(IsNotCommand(), CreateInstruction.Name)
async def process_instruction_add(message: Message, state: FSMContext):
    lang = extract_language(message)
    title = message.text

    if len(title) < 30:
        await state.update_data(title=title)
        await message.answer(get_message(lang, "sent_lang_instruction"))
        await state.set_state(CreateInstruction.Language)
    else:
        await message.answer(get_message(lang, "category_name_too_long"))
        return


# сохранение названия, языка и id категории в бд
@router.message(IsNotCommand(), CreateInstruction.Language)
async def add_category_language(message: Message, state: FSMContext):
    lang = extract_language(message)
    user_id = message.from_user.id
    language = message.text.lower()
    state_data = await state.get_data()
    group_id = state_data.get('group_id')
    title = state_data.get('title')
    group_name = state_data.get('group_name')
    image_url = state_data.get('image_url')
    code = await generate_random_string_async_lower(8)

    existing_instruction = await check_instruction(user_id, title, group_id)
    if existing_instruction:
        msg = get_message(lang, "instruction_already_exists_message")
        await message.answer(msg)
        return

    if is_valid_language_code(language):
        try:
            await add_instruction(user_id, title=title, group_id=group_id, group_name=group_name, image_url=image_url, language=language, code=code)
            await message.answer(get_message(lang, "instruction_added_message"))
            await state.clear()
        except IntegrityError as e:
            await message.answer(get_message(lang, "instruction_added_error"))
    else:
        error_msg = get_message(lang, "invalid_language_code")
        await message.answer(error_msg)
