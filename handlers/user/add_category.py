# handlers/user/add_category.py
import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from Filter.Filter import IsNotCommand, is_valid_language_code
from database.add_to_db import add_category
from database.get_to_db import get_user, get_user_instructions_with_cache
from loader import dp
from lang.get_message import get_message, extract_language
from states.user_states import CreateCategory
from keyboards.inline.categories_keyboards import instructions_keyboard
from utils.code_generator import generate_random_string_async_lower
from config_data.config import ADMIN_IDS

router = Router()
dp.include_router(router)


# команда add_category
@router.message(Command('add_category'))
async def add_category_command(message: Message, state: FSMContext):
    lang= extract_language(Message)
    user_id = message.from_user.id
    user_data = await get_user(user_id)
    if user_data['type'] in ["creator", "admin" , "user", "pro"]:
        instructions = await get_user_instructions_with_cache(user_id)
        print(len(instructions))

        if not instructions:
            await message.answer(get_message(lang, "not_instruction_default"))
            return
        
        await message.answer(get_message(lang, "micro_plan_add_category"))
        await asyncio.sleep(2)
        
        inline_kb = instructions_keyboard(instructions, "chooseInstruction", "help", 1)
        msg = get_message(lang, "choose_instruction")
        await message.answer(msg, reply_markup=inline_kb)
        await state.set_state(CreateCategory.InstructionId)
    


# когда категория выбрана - запрос названия
@router.callback_query(F.data.startswith('chooseInstruction:'), CreateCategory.InstructionId)
async def choose_instruction_callback(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    instruction_id = call.data.split(':')[1]
    await state.update_data(instruction_id=instruction_id)
    
    msg = get_message(lang, "sent_name_category")
    await call.message.edit_text(msg, reply_markup=None)
    await state.set_state(CreateCategory.Name)




# приём и сохранение названия категории
@router.message(IsNotCommand(), CreateCategory.Name)
async def add_category_name(message: Message, state: FSMContext):
    lang = extract_language(message)
    name = message.text.strip()
    state_data = await state.get_data()
    instruction_id = state_data.get("instruction_id")
    code = await generate_random_string_async_lower(12)

    if len(name) > 40:
        error_msg = get_message(lang, "category_name_too_long")
        await message.answer(error_msg)
        return

    await add_category(instruction_id, name, code)
    await message.answer(get_message(lang, "category_crating"))    
    await asyncio.sleep(1)
    await state.set_state(CreateCategory.Name)
    await message.answer(get_message(lang, "sent_name_category"))




# сохранение названия, языка и id категории в бд
@router.message(IsNotCommand(), CreateCategory.Language)
async def add_category_language(message: Message, state: FSMContext):
    lang = extract_language(message)
    language = message.text.lower()
    state_data = await state.get_data()
    name = state_data.get("name")
    instruction_id = state_data.get("instruction_id")

    if is_valid_language_code(language):
        code = await generate_random_string_async_lower(12)
        await add_category(instruction_id, name, language, code)
        await message.answer(get_message(lang, "category_crating"))
        await asyncio.sleep(1)
        await state.set_state(CreateCategory.Name)
        await message.answer(get_message(lang, "sent_name_category"))

    else:
        error_msg = get_message(lang, "invalid_language_code")
        await message.answer(error_msg)


