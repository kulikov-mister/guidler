from aiogram import Router, Bot, F
from aiogram.types import Message, InlineKeyboardButton, WebAppInfo, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from config_data.config import ADMIN_IDS
from lang.get_message import get_message, extract_language
from loader import dp

router = Router()
dp.include_router(router)


@router.message(Command('help'))
async def start(message: Message):
    lang= extract_language(Message)
    await message.answer(get_message(lang, "help_message"))
    

@router.message(Command('ai'))
async def open_webapp(message: Message):
    ikb_donate = InlineKeyboardMarkup(row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Открыть AI', web_app=WebAppInfo(url=f'https://mindpoint.kz/ai'))
            ]
        ])

    await message.answer("Нажмите кнопку, чтобы открыть приложение", reply_markup=ikb_donate)


@router.callback_query(F.data.in_(('mainstart_help', 'help')))
async def cancel(call: CallbackQuery, state: FSMContext):
    lang= extract_language(call)
    await state.clear()
    msg = get_message(lang, "help_message")
    await call.answer("✅")
    await call.message.edit_text(msg)
    
    
@router.message(Command('cancel'), F.from_user.id.in_(ADMIN_IDS))
async def cancel(message: Message, state: FSMContext):
    lang= extract_language(message)
    await state.clear()
    await message.answer(get_message(lang, "cancel_message"))
    
    
@router.callback_query(F.data=="delete")
async def delete(call: CallbackQuery, state: FSMContext):
    await call.answer("✅")
    await state.clear()
    await call.message.delete()