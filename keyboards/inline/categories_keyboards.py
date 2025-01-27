from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.inline_builder import get_paginated_keyboard


# Создание кнопок с категориями
def categories_keyboard(categories, cb_prefix: str, cb_back_button: str, page: int = 1, items_per_page: int = 7) -> InlineKeyboardMarkup:
    buttons = []

    for category in categories:
        button_text = category['name']
        callback_data = f"{cb_prefix}:{category['id']}:-"

        buttons.append(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Создаем пагинированную клавиатуру
    return get_paginated_keyboard(buttons, page, cb_back_button, cb_prefix, items_per_page)


# создание кнопок с инструкциями
def instructions_keyboard(instructions, cb_prefix: str, cb_back_button: str, page: int = 1, items_per_page: int = 7, r: int = None) -> InlineKeyboardMarkup:
    
    buttons = []
    if r == 1:
        buttons.append(InlineKeyboardButton(text="Без категории", callback_data=f"{cb_prefix}::-"))

    for instruction in instructions:
        buttons.append(
            InlineKeyboardButton(text=instruction['title'], callback_data=f"{cb_prefix}:{instruction['id']}:-")
        )

    r = f"{cb_prefix}:{instruction['id']}:-" if r == 2 else (f"{cb_prefix}::-" if r == 3 else None)
    return get_paginated_keyboard(buttons, page, cb_back_button, cb_prefix, items_per_page, r)



# Создание кнопок с постами для множественного выбора
def posts_keyboard(posts, selected_posts, cb_prefix: str, cb_back_button: str, page: int = 1, items_per_page: int = 7, r: str = None) -> InlineKeyboardMarkup:
    buttons = []

    for post in posts:
        button_text = post['name']  
        is_selected = post['id'] in selected_posts
        selection_mark = "✅" if is_selected else "❌"
        callback_data = f"{cb_prefix}:{post['id']}:{'remove' if is_selected else 'add'}"

        buttons.append(
            InlineKeyboardButton(text=f"{selection_mark} {button_text}", callback_data=callback_data)
        )
    return get_paginated_keyboard(buttons, page, cb_back_button, cb_prefix, items_per_page, r)



# Создание кнопок с постами для просмотра
def posts_view_keyboard(posts, active_post_id, cb_prefix: str, cb_back_button: str, prefix= None, r= None) -> InlineKeyboardMarkup:
    max_buttons = 7
    active_post_index = next((i for i, post in enumerate(posts) if post['id'] == active_post_id), -1)
    total_posts = len(posts)

    # Определяем диапазон отображаемых кнопок
    start_index = max(0, min(active_post_index - max_buttons // 2, total_posts - max_buttons))
    end_index = min(start_index + max_buttons, total_posts)

    buttons = []
    for index in range(start_index, end_index):
        button_text = str(index + 1)
        if index == active_post_index:
            button_text = f"•{button_text}•"
        callback_data = f"{cb_prefix}:{posts[index]['id']}:{prefix}"
        buttons.append(InlineKeyboardButton(text=button_text, callback_data=callback_data))

    if r == "my_posts":
        edition_buttons = []
        edition_buttons.append(InlineKeyboardButton(text="✏️", callback_data=f"editPost:name:{active_post_id}"))
        edition_buttons.append(InlineKeyboardButton(text="📝", callback_data=f"editPost:desc:{active_post_id}"))
        edition_buttons.append(InlineKeyboardButton(text="🖼️", callback_data=f"editPost:pic:{active_post_id}"))
        edition_buttons.append(InlineKeyboardButton(text="🗑️", callback_data=f"editPost:delete:{active_post_id}"))

    navigation_buttons = []

    if active_post_index > 0:
        prev_post_id = posts[active_post_index - 1]['id']
        navigation_buttons.append(InlineKeyboardButton(text="◀️", callback_data=f"{cb_prefix}:{prev_post_id}:{prefix}"))
    navigation_buttons.append(InlineKeyboardButton(text="🏡", callback_data=cb_back_button))
    if active_post_index < total_posts - 1:
        next_post_id = posts[active_post_index + 1]['id']
        navigation_buttons.append(InlineKeyboardButton(text="▶️", callback_data=f"{cb_prefix}:{next_post_id}:{prefix}"))

    keyboard_builder = InlineKeyboardBuilder()
    for button in buttons:
        keyboard_builder.add(button)
    
    if r == "my_posts":
        keyboard_builder.row(*edition_buttons)
    keyboard_builder.row(*navigation_buttons)

    return keyboard_builder.as_markup()


