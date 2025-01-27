# /Users/aleksandrkulikov/Desktop/Python/Guidler/main.py
import asyncio
import logging
from loader import dp, bot
import handlers

# Инициализируем логгер
logger = logging.getLogger(__name__)

# Конфигурируем логирование
logging.basicConfig(
    level=logging.DEBUG,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
            '[%(asctime)s] - %(name)s - %(message)s')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
