# handlers/admin/updater.py
from aiogram import F, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from Filter.Filter import IsAdmin
from loader import dp, bot
from states.admin_states import update_state
import subprocess, os, time, tempfile


router = Router()
dp.include_router(router)


@router.message(Command("update"), IsAdmin())
async def update_command_handler(message: Message, state: FSMContext):
    await state.set_state(update_state.SendUpd)
    await message.answer('Пришлите файлы бота')



@router.message(F.document, update_state.SendUpd, IsAdmin())
async def document_handler(message: Message):
    document = message.document
    file_id = document.file_id
    file = await bot.get_file(file_id)

    relative_path = document.file_name
    bot_directory = os.path.expanduser('~/Guidler')

    # Ищем существующий файл в директории бота
    for root, dirs, files in os.walk(bot_directory):
        if relative_path in files:
            absolute_path = os.path.join(root, relative_path)
            await bot.download_file(file.file_path, destination=absolute_path)
            await message.reply(f"Файл {relative_path} обновлен в директории:\n<code>{absolute_path}</code>")
            break
    else:
        await message.reply(f"Файл {relative_path} не найден в директории бота.")


@router.message(Command("restart"), IsAdmin())
async def restart_command_handler(message: Message):
    await message.answer("Перезапускаю бота...")
    await dp.stop_polling()
    time.sleep(3)  # Задержка в 3 секунды
    subprocess.call(['sudo', 'systemctl', 'restart', 'guidler.service'])




@router.message(Command("logs"), IsAdmin())
async def logs_command(message: Message):
    try:
        log_file_path = 'bot_logs.log'

        log_file = FSInputFile(log_file_path)

        await message.answer_document(log_file, caption="Вот логи за последнюю минуту")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")


@router.message(Command("get_db"), IsAdmin())
async def get_db_command(message: Message):
    try:
        log_file_path = './database/guidler.db'

        log_file = FSInputFile(log_file_path)

        await message.answer_document(log_file, caption="Вот база данных")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")


@router.message(Command("clear_logs"), IsAdmin())
async def clear_logs_command(message: Message):
    try:
        log_file_path = 'bot_logs.log'
        os.remove(log_file_path)
        await message.answer(f"Логи успешно удалены!")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
        
        
@router.message(Command("send_logs"), IsAdmin())
async def send_logs_command(message: Message):
    try:
        log_file_path = 'bot_logs.log'
        with open(log_file_path, 'r') as file:
            last_lines = file.readlines()[-10:]

        fd, temp_file_path = tempfile.mkstemp(suffix=".log")
        with open(fd, 'w') as temp_file:
            temp_file.writelines(last_lines)
        await message.answer_document(FSInputFile(temp_file_path), caption="Последние 10 строк логов")
        os.remove(temp_file_path)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
