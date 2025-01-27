from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton
from loader import dp

router = Router()
dp.include_router(router)

def get_main_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="🏠 Главное меню"),
    )
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

