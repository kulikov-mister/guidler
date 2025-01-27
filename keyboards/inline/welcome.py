from keyboards.inline_builder import inline_builder
from lang.get_message import get_keyboard



def generate_welcome_keyboard(language: str):
    buttons_data = [
        {"key": "user_button", "callback_data": "user"},
        {"key": "creator_button", "callback_data": "creator"},
        [
            {"key": "price_button", "callback_data": "price"},
            {"key": "support_button", "callback_data": "support"}
        ],
    ]

    return inline_builder(buttons_data, language)