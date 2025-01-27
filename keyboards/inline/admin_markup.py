from keyboards.inline_builder import inline_builder


# Данные кнопок для разметки администратора
admin_buttons_data = [
    {"text": "📨 Рассылка", "callback_data": 'admin_broadcast'},
    {"text": "🗂 Информация об авторах", "callback_data": 'info_creators'},
]


def markup_admin():
    return inline_builder(admin_buttons_data)