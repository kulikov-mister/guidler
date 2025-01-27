# lang/get_message.py
import importlib, logging
from aiogram.types import Message, CallbackQuery, InlineQuery, User, ChatMemberUpdated


# вытаскивает язык пользователя из полученного апдейта
def extract_language(update: User | Message | CallbackQuery | InlineQuery | ChatMemberUpdated) -> str:
    user = getattr(update, 'from_user', None)
    return (user.language_code or 'ru').lower() if user else 'ru'


# ______________________________________________________________________________ #

# берет сообщение для пользователя по языку
def get_message(language: str, message_key: str,  **format_args) -> str:
    """
    Получает строку перевода по ключу для указанного языка и директории.

    :param language: Код языка, например 'en' или 'ru'.
    :param message_key: Ключ строки перевода.
    :return: Строка перевода.
    """
    try:
        # Пытаемся импортировать модуль для заданного языка
        messages_module = importlib.import_module(f"lang.messages.{language}")
    except ModuleNotFoundError:
        try:
            # Пытаемся загрузить русский язык по умолчанию
            messages_module = importlib.import_module("lang.messages.ru")
        except ModuleNotFoundError:
            # Логируем ошибку, если не найден ни указанный язык, ни русский
            logging.error(f"Языковые модули не найдены: {language} и русский")
            return ""

    # Получаем словарь переводов из модуля
    messages_dict = getattr(messages_module, language, None)

    # Возвращаем строку перевода, если она существует, иначе пустую строку
    return messages_dict.get(message_key, "").format(**format_args)


# берет текст кнопки для пользователя по языку
def get_keyboard(language: str, keyboard_key: str,  **format_args) -> str:
    """
    Получает текст кнопки по ключу для указанного языка и директории.

    :param language: Код языка, например 'en' или 'ru'.
    :param keyboard_key: Ключ текста кнопки.
    :return: Текст кнопки.
    """
    try:
        keyboards_module = importlib.import_module(f"lang.keyboards.{language}")
    except ModuleNotFoundError:
        try:
            # Пытаемся загрузить русский язык по умолчанию
            keyboards_module = importlib.import_module("lang.keyboards.ru")
        except ModuleNotFoundError:
            # Логируем ошибку, если не найден ни указанный язык, ни русский
            logging.error(f"Языковые модули не найдены: {language} и русский")
            return ""

    keyboards_dict = getattr(keyboards_module, language, None)


    # Возвращаем текст кнопки или пустую строку, если ключ не найден
    return keyboards_dict.get(keyboard_key, "").format(**format_args)
