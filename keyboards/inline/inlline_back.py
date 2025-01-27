# keyboards/inline/inlline_back.py
from keyboards.inline_builder import inline_builder

# кнопка назад
def user_back_keyboard():
    buttons_data = [{"text": "🏠 Главное меню", "callback_data": "mainstart"}]
    return inline_builder(buttons_data)

# кнопка назад из админки
def admin_back_keyboard():
    buttons_data = [{"text": "🏠 Главное меню", "callback_data": "mainstart_company"}]
    return inline_builder(buttons_data)

# кастомная кнопка назад
def back_keyboard(callback_data: str):
    buttons_data = [{"text": "🔙 Назад", "callback_data": callback_data}]
    return inline_builder(buttons_data)


# кастомная кнопка для удаления
def approve_delete_keyboard(callback_data: str, id, lang):
    buttons_data = [
        {"key": "approve_delete", "callback_data": f"{callback_data}:{id}"},
        {"key": "cancel", "callback_data": f"post_view:{id}:"},
    ]
    return inline_builder(buttons_data, lang)


def return_keyboard(id, lang):
    buttons_data = [
        {"key": "return_posts", "callback_data": f"post_view:{id}:"},
    ]
    return inline_builder(buttons_data, lang)