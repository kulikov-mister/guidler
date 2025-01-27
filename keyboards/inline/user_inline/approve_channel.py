# keyboards/inline/user_inline/approve_channel.py
from keyboards.inline_builder import inline_builder


def keyboard_approve_channel(lang, group_id, group_name):
    return inline_builder(
        [{"key": "approve_channel", "callback_data": f"#ch_{group_id}_{group_name}"}], lang)
