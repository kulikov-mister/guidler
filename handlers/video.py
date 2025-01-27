from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from Filter.Filter import IsNotCommand
from database.add_to_db import add_category
from database.get_to_db import get_user
from keyboards.inline.welcome import generate_welcome_keyboard
from keyboards.inline.inlline_back import back_keyboard
from loader import dp
from lang.get_message import get_message, extract_language
from states.user_states import CreateCategory
from keyboards.inline.categories_keyboards import categories_keyboard



router = Router()
dp.include_router(router)


@router.message(F.video | F.animation)
async def video_handler(message: Message):
    file_id = message.animation.file_id or message.video.file_id
    await message.answer(file_id)

