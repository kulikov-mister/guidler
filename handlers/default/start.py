# handlers/default/start.py
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from Filter.Filter import IsNotCommand
from database.add_to_db import add_user
from database.get_to_db import get_user
from keyboards.inline.welcome import generate_welcome_keyboard
from loader import dp
from lang.get_message import get_message, extract_language
from utils.set_bot_commands import set_default_commands
from utils.cache_utils import CacheManager
from config_data.config import ADMIN_IDS

router = Router()
dp.include_router(router)
cache_manager = CacheManager()


# команда старт
@router.message( CommandStart(deep_link=False, magic=F.args == None) )
async def start(message: Message, state: FSMContext):
    lang = extract_language(message)
    user_id = message.from_user.id
    await state.clear()

    user_data = await get_user(user_id)
    if user_data is None:
        # Пользователь не найден в кеше и БД
        if user_id in ADMIN_IDS:
            # Если пользователь - админ, но не зарегистрирован
            await add_user(user_id, message.chat.full_name, "admin")
            msg = get_message(lang, "start_admin_message")
            inline_kb = None
            await set_default_commands(user_id, "admin")
        else:
            # Незарегистрированный обычный пользователь
            msg = get_message(lang, "welcome_message")
            inline_kb = generate_welcome_keyboard(lang)
            await set_default_commands(user_id, "user")
    else:
        # Зарегистрированный пользователь (включая админа)
        if user_id in ADMIN_IDS:
            await set_default_commands(user_id, "admin")
        else:
            await set_default_commands(user_id, "user")
        msg = get_message(lang, "start_admin_message" if user_data['type'] == "admin" else "start_message")
        inline_kb = None

        try:
            await message.answer_animation(
                caption=msg, 
                animation="CgACAgIAAxkBAAIBBGW3ZskTnkgzPD8o3pSCm0xfuHs0AAK9OwACU8m5SR4ZfirPwOS9NAQ",
                reply_markup=inline_kb
                )
        except:
            await message.answer_animation(
                caption=msg, 
                animation="CgACAgIAAxkBAAICC2XTFas3RznkYmwaUN27JQZpe0-eAAK7OgACh0C4Sfc24fzHEGF2NAQ",
                reply_markup=inline_kb
                )



# регистрация юзера
@router.callback_query(F.data == 'user')
async def process_callback_user(call: CallbackQuery, state: FSMContext):
    await call.answer("✅")    
    user_id = call.message.chat.id
    user_data = await get_user(user_id)
    if not user_data:
        name = call.message.chat.full_name
        await add_user(user_id, name, "user")
    await call.message.delete()
    await call.message.answer_animation(
        caption='🔆 Добро пожаловать!', 
        animation="CgACAgIAAxkBAAIBBGW3ZskTnkgzPD8o3pSCm0xfuHs0AAK9OwACU8m5SR4ZfirPwOS9NAQ"
        )



# регистрация автора
@router.callback_query(F.data == 'creator')
async def process_callback_creator(call: CallbackQuery, state: FSMContext):
    await call.answer("✅")    
    user_id = call.message.chat.id
    name = call.message.chat.full_name
    user_data = await get_user(user_id)
    
    if not user_data:
        add_user(user_id, name, "creator")

    await call.message.delete()
    await call.message.answer_animation(
        caption='🔆 Добро пожаловать!',
        animation="CgACAgIAAxkBAAIBBGW3ZskTnkgzPD8o3pSCm0xfuHs0AAK9OwACU8m5SR4ZfirPwOS9NAQ"
        )

