from typing import List
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lang.get_message import get_keyboard


# создание инлайн кнопок
def inline_builder(buttons: List[dict], language: str) -> InlineKeyboardMarkup:
    inline_keyboard = []

    for item in buttons:
        if isinstance(item, list):
            row = [InlineKeyboardButton(text=get_keyboard(language, button["key"]), callback_data=button["callback_data"]) for button in item]
            inline_keyboard.append(row)
        else:
            button_text = get_keyboard(language, item["key"])
            inline_btn = InlineKeyboardButton(text=button_text, callback_data=item["callback_data"])
            inline_keyboard.append([inline_btn])
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)



# добавление кнопок пагинации к основному список кнопок
def get_paginated_keyboard(buttons: list[InlineKeyboardButton], page: int, back_callback_data: str, cb_prefix: str, items_per_page: int = 7, r:str = None) -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    # Добавляем кнопки для текущей страницы
    for button in buttons[start_index:end_index]:
        if r == 3:
            keyboard_builder.add(button)
        else:
            keyboard_builder.row(button)

    # Добавляем кнопки навигации
    navigation_buttons = []
    # Кнопка "prev page", если текущая не первая страница
    if page > 1:
        navigation_buttons.append(InlineKeyboardButton(text=f" {page-1} ◀️", callback_data=f"page:{cb_prefix}:{page-1}"))
    # Кнопка "Назад" добавляется обязательно
    navigation_buttons.append(InlineKeyboardButton(text="🏡", callback_data=back_callback_data))
    if r in (1, 2):
        navigation_buttons.append(InlineKeyboardButton(text="✅", callback_data="confirm_order"))
    # Кнопка "next page", если не последняя страница
    if end_index < len(buttons):
        navigation_buttons.append(InlineKeyboardButton(text=f"▶️ {page+1} ", callback_data=f"page:{cb_prefix}:{page+1}"))
        
    # Добавляем ряд с кнопками навигации
    keyboard_builder.row(*navigation_buttons)

    return keyboard_builder.as_markup()


def get_paginated_posts_keyboard(len_posts: int, page: int, back_callback_data: str, cb_prefix: str) -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    
    # Добавляем кнопки навигации
    navigation_buttons = []
    # Кнопка "prev page", если текущая не первая страница
    if page > 0:
        navigation_buttons.append(InlineKeyboardButton(text=f" {page} ◀️", callback_data=f"page:{cb_prefix}:{page-1}"))
    # Кнопка "Назад" добавляется обязательно
    navigation_buttons.append(InlineKeyboardButton(text="🏡", callback_data=back_callback_data))
    # Кнопка "next page", если не последняя страница
    if page < len_posts-1:
        navigation_buttons.append(InlineKeyboardButton(text=f"▶️ {page+1} ", callback_data=f"page:{cb_prefix}:{page+1}"))
        
    # Добавляем ряд с кнопками навигации
    keyboard_builder.row(*navigation_buttons)

    return keyboard_builder.as_markup()
