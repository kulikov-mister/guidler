# keyboards/inline/instructions_keyboards.py
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline_builder import get_paginated_keyboard



# создание кнопок с инструкциями
def instructions_keyboard(instructions, cb_prefix: str, cb_back_button: str, page: int = 1, items_per_page: int = 7, r: int = None) -> InlineKeyboardMarkup:
    
    # Инициализация списка кнопок
    buttons = []
    # Добавляем кнопку "Без категории", если r равно 1
    if r == 1:
        buttons.append(InlineKeyboardButton(text="Без категории", callback_data=f"{cb_prefix}:"))

    for instruction in instructions:
        buttons.append(
            InlineKeyboardButton(text=instruction.title, callback_data=f"{cb_prefix}:{instruction.group_id}")
        )
    r = f"{cb_prefix}:{instruction.id}:-" if r == 2 else (f"{cb_prefix}::-" if r == 3 else None)

    return get_paginated_keyboard(buttons, page, cb_back_button, cb_prefix, items_per_page, r)