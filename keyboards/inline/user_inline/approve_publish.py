# keyboards/inline/user_inline/approve_publish.py
from keyboards.inline_builder import inline_builder


def keyboard_approve_publish(lang, prefix):
    return inline_builder(
        [{"key": "approve_publish", "callback_data": f"approve_publish_{prefix}"}], lang)
