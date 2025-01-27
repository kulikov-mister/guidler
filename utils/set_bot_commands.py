from aiogram.types import BotCommand, BotCommandScopeChat
from loader import bot
from config_data.config import ADMIN_IDS


async def set_default_commands(user_id, type):
    
    if user_id in ADMIN_IDS:
        commands = [
            BotCommand(command="start", description="Нажмите, чтобы начать! 🚀"),
            BotCommand(command="admin", description="Админ-панель"),
            BotCommand(command="help", description="Помощь! 📋"),
            BotCommand(command="add_instruction", description="Добавить инструкцию"),
            BotCommand(command="add_category", description="Добавить категорию"),
            BotCommand(command="add_faq", description="Добавить FAQ-пост"),
            BotCommand(command="publish", description="Опубликовать инструкции"),
            BotCommand(command="publish_category", description="Опубликовать категорию"),
            BotCommand(command="publish_all", description="Опубликовать инструкцию полностью"),
            BotCommand(command="my_posts", description="Мои посты"),
            BotCommand(command="logs", description="Файл с логами бота"),
            BotCommand(command="send_logs", description="Последние 10 логов бота"),
            BotCommand(command="clear_logs", description="Удалить логи бота"),
            BotCommand(command="get_db", description="Получить базу данных"),
            BotCommand(command="update", description="Обновить файлы бота"),
            BotCommand(command="restart", description="Перезапустить бота"),
            BotCommand(command="cancel", description="Отменить операцию"),
        ]
    else:
        if type:
            commands = [
                BotCommand(command="start", description="Нажмите, чтобы начать! 🚀"),
                BotCommand(command="help", description="Помощь! 📋"),
                BotCommand(command="add_instruction", description="Добавить инструкцию"),
                BotCommand(command="add_category", description="Добавить категорию"),
                BotCommand(command="add_faq", description="Добавить FAQ-пост"),
                BotCommand(command="publish", description="Опубликовать инструкции"),
                BotCommand(command="publish_all", description="Опубликовать инструкцию полностью"),
                BotCommand(command="my_posts", description="Мои посты"),
                BotCommand(command="cancel", description="Отменить операцию"),
            ]
        else:
            commands = [
                BotCommand(command="start", description="Нажмите, чтобы начать! 🚀")
            ]

    await bot.set_my_commands(commands, scope=BotCommandScopeChat(chat_id=user_id))

