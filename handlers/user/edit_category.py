# handlers/user/edit_posts.py
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from Filter.Filter import IsNotCommand
from database.update_to_db import update_category
from database.delete_from_db import delete_post_by_id
from loader import dp
from lang.get_message import get_message, extract_language
from states.user_states import EditCategory


router = Router()
dp.include_router(router)


# команда редактирования категории
@router.message(Command("edit_categoty"))
async def edit_data_post(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    ...
    