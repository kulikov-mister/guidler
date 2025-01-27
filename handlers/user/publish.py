# handlers/user/publicate.py
import asyncio
import flag
from aiogram import F, Router
from aiogram.utils.deep_linking import create_start_link
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from database.get_to_db import (
    get_user, get_categories_with_cache, get_user_instructions_with_cache, get_posts_by_category_id, get_category_by_id,
    get_instruction_by_id
)
from database.add_to_db import add_published_page
from loader import dp, bot
from lang.get_message import get_message, extract_language
from states.user_states import Publish
from keyboards.inline.categories_keyboards import instructions_keyboard, categories_keyboard, posts_keyboard
from keyboards.inline.user_inline.publish_type import keyboard_publish_type



router = Router()
dp.include_router(router)


# функция создания диплинков инструкций к посту
async def linksPost_creator(posts, id_published, catName, catCode, flag, pages: int, r: int = None):
    """
    Формирует сообщение со ссылками на посты.

    :param posts: список постов
    :param catName: название категории
    :param bot: экземпляр бота для создания диплинков
    :return: сформированное сообщение
    """
    deep_link = await create_start_link(bot, payload=catCode)
    link_bot = await create_start_link(bot, payload="")
    if catName and catCode and flag:
        if r:
            base_link = deep_link
        else:
            base_link = link_bot
        link_category = f"<a href='{base_link}'><b>{catName}</b></a>"
        message = f"{flag} <b>{link_category}</b>\n\n"
    else:
        message = ""

    for index, post in enumerate(posts, start=1):
        # Создаем диплинк для каждого поста
        deep_link = await create_start_link(bot, payload=f"{id_published}_{post.code}")
        page = index + pages
        message += f"{page}. <a href='{deep_link}'>{post.name}</a>\n"

    return message


# разделитель постов
def chunk_posts(posts, chunk_size):
    """Разделяет список posts на подсписки размером chunk_size."""
    for i in range(0, len(posts), chunk_size):
        yield posts[i:i + chunk_size]


# функция создает страницы в виде диплинков к посту
async def pagesPost_creator(total_pages, base_link, base_message_id, index):
    """
    Формирует строку с ссылками на страницы постов.

    :param total_pages: общее количество страниц
    :param base_message_id: ID начального сообщения
    :param username: имя пользователя или название канала
    :return: сформированное сообщение
    """
    message = "•"
    for page_number in range(1, total_pages + 1):
        # Создаем ссылку на каждую страницу, увеличивая message_id на 1 для каждой следующей страницы
        current_message_id = base_message_id + (page_number - 1)
        page_link = f"{base_link}/{current_message_id}"
        
        # если текущая страница равна индексу то пишем страницу без ссылки
        if page_number == index:
            message += f" {page_number} •"
        else:
            message += f" <a href='{page_link}'>{page_number}</a> •"
    
    return message


# Функция для сортировки постов по выбранному порядку
def sort_posts_by_order(posts, selected_order):
    sorted_posts = []
    # Ищем посты в заданном порядке и добавляем их в новый список
    for post_id in selected_order:
        for post in posts:
            if post.id == post_id:
                sorted_posts.append(post)
                break
    return sorted_posts


# ------------------------------------------------------------------------------------------------------------------ #


# команда publish
@router.message(Command('publish', 'publish_all'))
async def publish_command(message: Message, state: FSMContext):
    lang= extract_language(Message)
    user_id = message.from_user.id
    user_data = await get_user(user_id)

    if user_data['type'] in ["creator", "admin" , "user", "pro"]:
        instructions = await get_user_instructions_with_cache(user_id)

        if not instructions:
            await message.answer(get_message(lang, "not_instruction_for_publish"))
            return
        
        inline_kb = instructions_keyboard(instructions, "chooseInstruction", "help", 1)
        await message.answer(get_message(lang, "micro_plan_publish"))
        await asyncio.sleep(1)

        await message.answer(
            get_message(lang, "choose_instruction"),
            reply_markup=inline_kb
            )
        if message.text == '/publish':
            await state.set_state(Publish.InstructionId)
        elif message.text == '/publish_all':
            await state.set_state(Publish.InstructionIdAll)
        
    elif not user_data:
        await message.answer(get_message(lang, "registration_required_message"))
        return


# колбек publish
@router.callback_query(F.data.in_(['publish', 'publish_all']))
async def publish_collback(call: CallbackQuery, state: FSMContext):
    lang= extract_language(call)
    user_id = call.from_user.id

    await call.answer("✅")
    instructions = await get_user_instructions_with_cache(user_id)

    if not instructions:
        await call.message.edit_text(get_message(lang, "not_instruction_for_publish"))
        return
    
    inline_kb = instructions_keyboard(instructions, "chooseInstruction", "help", 1)
    await call.message.edit_text(get_message(
        lang, "choose_instruction"), reply_markup=inline_kb
        )
    await state.set_state(Publish.InstructionId)


# Пользователь выбирает инструкцию
@router.callback_query(F.data.startswith('chooseInstruction:'), StateFilter(Publish.InstructionId, Publish.InstructionIdAll, Publish.CategoryId, Publish.CategoryIdAll, Publish.ChoosePostsOrder))
async def select_instruction(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    instruction_id = call.data.split(":")[1]
    current_state = await state.get_state()

    if instruction_id:
        instruction_data =  await get_instruction_by_id(instruction_id)
        await state.update_data(instruction_id=instruction_id, group_id=instruction_data.group_id)
        
        categories = await get_categories_with_cache(instruction_id)
        if categories:

            if current_state == "Publish:InstructionId":
                await state.set_state(Publish.CategoryId)
                kb_back = 'publish'
            elif current_state == "Publish:InstructionIdAll":
                await state.set_state(Publish.CategoryIdAll)
                kb_back = 'publish_all'

            inline_kb = categories_keyboard(categories, "chooseCategory", kb_back, 1)
            await call.message.edit_text(get_message(lang, "choose_category"), reply_markup=inline_kb)
            await call.answer("✅")
        else:
            await call.answer(get_message(lang, "not_categories_for_faq"), show_alert=1)



# Пользователь выбирает категорию
@router.callback_query(F.data.startswith('chooseCategory:'), StateFilter(Publish.CategoryId, Publish.CategoryIdAll))
async def select_category(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    category_id = call.data.split(':')[1]
    user_id = call.from_user.id
    await state.update_data(category_id=category_id)
    user_data = await get_user(user_id)
    current_state = await state.get_state()
    
    if user_data['type'] in ["admin", "pro"]:

        msg = get_message(lang, "select_type_for_publish_pro")
        inline_kb = keyboard_publish_type(lang, 2)

    if user_data['type'] in ["creator", "user"]:
        msg = get_message(lang, "select_type_for_publish_not_pro")
        inline_kb = keyboard_publish_type(lang, 1)


    posts = await get_posts_by_category_id(category_id)
    await state.update_data(posts=posts)
    formatted_posts = [{'id': post.id, 'name': post.name} for post in posts]
    state_data = await state.get_data()
    instruction_id = state_data.get("instruction_id")

    # Измененная логика для selected_posts_order
    if current_state == "Publish:CategoryId":
        selected_posts_order = []
    elif current_state == "Publish:CategoryIdAll":
        selected_posts_order = [post['id'] for post in formatted_posts]
        await state.update_data(selected_posts_order=selected_posts_order)

    base_message = get_message(lang, "current_selected_post")

    preview_message = ""
    for index, post_id in enumerate(selected_posts_order, start=1):
        post_name = next((post['name'] for post in formatted_posts if post['id'] == post_id), None)
        preview_message += f"{index}. {post_name}\n"

    while len(preview_message) > 3900:
        selected_posts_order.pop(0)
        preview_message = ""
        for index, post_id in enumerate(selected_posts_order, start=1):
            post_name = next((post['name'] for post in formatted_posts if post['id'] == post_id), None)
            preview_message += f"{index}. {post_name}\n"

    preview_message = base_message + preview_message


    cb_data = f'chooseInstruction:{instruction_id}:-'
    inline_kb = posts_keyboard(formatted_posts, selected_posts_order, 'choosePost', cb_data, r=2)

    await call.message.edit_text(preview_message, reply_markup=inline_kb)
    await call.answer("✅")
    await state.set_state(Publish.ChoosePostsOrder)


# выбор постов для публикации
@router.callback_query(F.data.startswith('choosePost:'), Publish.ChoosePostsOrder)
async def handle_post_selection(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    user_id = call.message.from_user.id
    post_id, action = call.data.split(':')[1:]  
    post_id = int(post_id)
    page = 1
    navigation_buttons = call.message.reply_markup.inline_keyboard[-1]
    for button in navigation_buttons:
        button_data = button.callback_data
        if button_data.startswith("page:"):
            page = int(button_data.split(':')[2])
            if "▶️" in button.text:
                page -= 1
            elif "◀️" in button.text:
                page += 1
            break
        
    state_data = await state.get_data()
    selected_posts_order = state_data.get("selected_posts_order", [])
    if action == 'add' and post_id not in selected_posts_order:
        selected_posts_order.append(post_id)
    elif action == 'remove' and post_id in selected_posts_order:
        selected_posts_order.remove(post_id)
    await state.update_data(selected_posts_order=selected_posts_order)

    posts = state_data.get("posts")
    formatted_posts = [{'id': post.id, 'name': post.name} for post in posts]
    instruction_id = state_data.get("instruction_id")
    cb_data = f'chooseInstruction:{instruction_id}:-'
    base_message = get_message(lang, "current_selected_post")

    preview_message = ""
    for index, post_id in enumerate(selected_posts_order, start=1):
        post_name = next((post['name'] for post in formatted_posts if post['id'] == post_id), None)
        preview_message += f"{index}. {post_name}\n"

    while len(preview_message) > 3900:
        selected_posts_order.pop(0)
        preview_message = ""
        for index, post_id in enumerate(selected_posts_order, start=1):
            post_name = next((post['name'] for post in formatted_posts if post['id'] == post_id), None)
            preview_message += f"{index}. {post_name}\n"

    preview_message = base_message + preview_message
    inline_kb = posts_keyboard(formatted_posts, selected_posts_order, 'choosePost', cb_data, page, r=2)
    await call.answer("✅")
    await call.message.edit_text(preview_message, reply_markup=inline_kb)



# подтверждение выбора постов и публикация
@router.callback_query(F.data == 'confirm_order', Publish.ChoosePostsOrder)
async def confirm_order(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call) #  язык пользователя
    state_data = await state.get_data() #  данные пользователя
    user_id = call.message.from_user.id # id пользователя
    user_data = await get_user(user_id)
    print(user_data)
    selected_posts_order = state_data.get("selected_posts_order", []) # выбранный порядок постов
    posts = state_data.get("posts") #  посты пользователя
    sorted_posts = sort_posts_by_order(posts, selected_posts_order)
    instruction_id = state_data.get("instruction_id")
    category_id = state_data.get("category_id") # id категории
    group_id = state_data.get("group_id") # id группы
    instrInfo = await get_instruction_by_id(instruction_id)
    instrLanguage = instrInfo.language if instrInfo else None  # Извлечение языка из инструкции
    catInfo = await get_category_by_id(category_id)
    catName = catInfo.name # название категории
    catCode = catInfo.code # код категории
    instrFlag = flag.flag(instrLanguage) # флаг из категории
    len_posts = len(sorted_posts) # количество постов
    qt_posts = 12 # количество постов на странице
    chunked_posts = list(chunk_posts(sorted_posts, qt_posts)) # деление постов на страницы
    pages = len(chunked_posts) # страниц у постов
    
    await call.answer("✅")

    if group_id:
        chat_member = await bot.get_chat_member(chat_id=group_id, user_id=bot.id)
        
        if chat_member.status == "administrator":
            # если пользователь pro посты постятся в группу без рекламы бота
            preview = False if user_data and user_data['type'] in ["admin", "pro"] else True
                
            if len_posts > qt_posts:
                sent_message = await bot.send_message(group_id, "✅")
                postUrl = sent_message.get_url()
                message_id = int(postUrl.split("/")[-1])
                await bot.delete_message(group_id, message_id)
                base_link = postUrl.rsplit('/', 1)[0]

                for i in range(1, pages+1):
                    id_published = await add_published_page(user_id, instruction_id, category_id, selected_posts_order, i)
                    postsText = await linksPost_creator(chunked_posts[i-1], id_published, catName, catCode, instrFlag, pages+i)
                    pages_msg = await pagesPost_creator(pages, base_link, message_id+1, i)
                    msg = postsText + f"\n\n{pages_msg}"
                    sent_post = await bot.send_message(group_id, msg, disable_web_page_preview=preview)

            else:
                if chunked_posts:
                    id_published = await add_published_page(user_id, instruction_id, category_id, selected_posts_order, 0)
                    postsText = await linksPost_creator(chunked_posts[0], id_published, catName, catCode, instrFlag, 0)
                    sent_post = await bot.send_message(group_id, postsText, disable_web_page_preview=preview)

                else:
                    await call.message.answer(get_message(lang, "not_selected_posts"))
                    return
                
            msg = get_message(lang,"post_publiched") + "\n\n" + call.message.html_text
            await call.message.edit_text(msg, reply_markup=None)

        else:
            await call.message.answer(get_message(lang, "bot_not_admin_message"))
    else:
        await call.message.answer(get_message(lang, "post_not_published_msg"))



# хендлер на переключение страниц на уровнях
@router.callback_query(F.data.startswith("page:"), StateFilter(Publish.InstructionId, Publish.CategoryId, Publish.ChoosePostsOrder))
async def query_page_navigation(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    user_id = call.from_user.id
    parts = call.data.split(":")
    cb_prefix = parts[1]
    page = int(parts[-1])

    if cb_prefix == "chooseInstruction":
        instructions = await get_user_instructions_with_cache(user_id)
        inline_kb = instructions_keyboard(instructions, "chooseInstruction", "help", page)
    
    elif cb_prefix == "chooseCategory":
        instruction_id = await state.get_data('instruction_id')
        categories = await get_categories_with_cache(instruction_id)
        inline_kb = categories_keyboard(categories, "chooseCategory", "publish", page)

    elif cb_prefix == "choosePost":
        state_data = await state.get_data()
        selected_posts_order = state_data.get("selected_posts_order", [])
        posts = state_data.get("posts")
        instruction_id = state_data.get("instruction_id")
        cb_data = f'chooseInstruction:{instruction_id}:-'
        formatted_posts = [{'id': post.id, 'name': post.name} for post in posts]
        cb_data = f'chooseInstruction:{instruction_id}:-'
        inline_kb = posts_keyboard(formatted_posts, selected_posts_order, 'choosePost', cb_data, page, r=2)


    if inline_kb:
        await call.answer(get_message(lang, "page_alert") + page)
        await call.message.edit_reply_markup(reply_markup=inline_kb)

    else:
        await call.answer(get_message(lang, "navigation_error"))
    return
    


