# config_data/config.py
import os
from dotenv import load_dotenv, find_dotenv


SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///database/guidler.db"
CURRENCY = "$"

# PROXY_URL = "http://proxy.server:3128"

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()


# Инициализируем бота
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
ADMIN_IDS = [int(admin_id) for admin_id in ADMIN_ID.split(",")]
PROXY_URL = os.getenv('PROXY_URL')