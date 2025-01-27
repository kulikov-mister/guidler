from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import or_f
from keyboards.inline_builder import get_paginated_keyboard
from keyboards.inline.inlline_back import back_keyboard
from loader import dp
from config_data.config import CURRENCY


router = Router()
dp.include_router(router)

