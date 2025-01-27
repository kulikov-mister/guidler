# keyboards/inline/user_inline/publish_type.py
from keyboards.inline_builder import inline_builder


def keyboard_publish_type(lang, r):
    
    keyboards_data = [
            {"key": "publish_all", "callback_data": f"publish_all"},
            {"key": "publish_one", "callback_data": f"publish_one"},
            {"key": "delete_kb", "callback_data": "delete"}    
        ]
    if r!=1:
        return inline_builder(keyboards_data, lang)
    else:
        return inline_builder(keyboards_data[1:], lang)
