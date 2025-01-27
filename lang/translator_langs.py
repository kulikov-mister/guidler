# lang/translator_langs.py
import ast, os, asyncio, time
import concurrent.futures
from re import I
from typing import Dict, List, Union

import openai

OPENAI_COMPLETION_OPTIONS: Dict[str, Union[int, str, float]] = {
    "temperature": 0.7,
    "max_tokens": 2000,
    "top_p": 1,
    "model": "gpt-4-turbo-preview",
    "frequency_penalty": 0,
    "presence_penalty": 0,
}

OPENAI_TOKEN: str = "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"

INPUT_COST: float = 0.001 / 1000
OUTPUT_COST: float = 0.003 / 1000

COMMENT_KEY = "##comment_value##"

IGNORED_KEYS: List[str] = [

    COMMENT_KEY,
]


languages = {
    "English": "en",
    "Russian": "ru",
    "Arabic": "ar",
    "Belarusian": "be",
    "Catalan": "ca",
    "Croatian": "hr",
    "Czech": "cs",
    "Dutch": "nl",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Hebrew": "he",
    "Hungarian": "hu",
    "Indonesian": "id",
    "Italian": "it",
    "Kazakh": "kk",
    "Korean": "ko",
    "Malay": "ms",
    "Norwegian": "no",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Serbian": "sr",
    "Slovak": "sk",
    "Spanish": "es",
    "Swedish": "sv",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Uzbek": "uz"
}

def remove_newline_from_beginning(input_string):
    while input_string.startswith("\n"):
        input_string = input_string[1:]
    return input_string


class DictionaryParser:
    def parse_file(self, file_path: str) -> Dict[str, str]:
        # Получаем абсолютный путь к файлу
        full_path = os.path.abspath(file_path)
        print(f"Попытка открыть файл: {full_path}")
        
        # Проверка существования файла
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Файл не найден: {full_path}")
        
        with open(full_path, "r", encoding="utf-8") as file:
            file_content = file.read()
            dictionary = ast.literal_eval(file_content.split("=", 1)[1].strip())
        return dictionary

    def load_to_file(self, dictionary: Dict[str, str], file_path: str) -> None:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"{file_path.split('/')[-1].split('.')[0]} = {{\n")
            for key, value in dictionary.items():
                if "\n" in value or "'" in value:
                    formatted_value = '"""\n        ' + value.replace('\n', '\n        ') + '\n    """'
                else:
                    formatted_value = f'"""{value}"""'
                file.write(f"    '{key}': {formatted_value},\n")
            file.write("}\n")



class GptTranslator:
    client: openai.AsyncClient
    input_tokens: int = 0
    output_tokens: int = 0

    def __init__(self, api_key: str = OPENAI_TOKEN) -> None:
        self.client = openai.AsyncClient(api_key=api_key)

    async def translate(self, target_language: str, text: str) -> str:
        
        completition: openai.types.Completion = await self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"You application localization helper. You get text and send only translated text in result",
                },
                {
                    "role": "user",
                    "content": f"Translate {text} to {target_language}, be careful about syntax",
                },
            ],
            **OPENAI_COMPLETION_OPTIONS,
        )

        self.input_tokens += completition.usage.prompt_tokens
        self.output_tokens += completition.usage.completion_tokens

        return completition.choices[0].message.content

    def get_usage_price(self) -> float:
        return self.input_tokens * INPUT_COST + self.output_tokens * OUTPUT_COST



async def translate_dictionary(
    translated_dict_path: str,
    translate_language: str,
    main_dict_path: str,
    print_logs: bool = True,
    use_ignored_keys: bool = False
) -> None:
    parser = DictionaryParser()
    translator = GptTranslator()

    # Проверка наличия файла перевода
    existing_translations = {}
    if os.path.exists(translated_dict_path):
        existing_translations = parser.parse_file(file_path=translated_dict_path)

    # Загрузка исходного словаря
    dictionary = parser.parse_file(file_path=main_dict_path)

    ignored_keys = IGNORED_KEYS if use_ignored_keys else []
    counter = 0
    t1 = time.time()
    number_of_values = len(dictionary) - len(ignored_keys)

    for key, value in dictionary.items():
        if key.strip() not in ignored_keys and key not in existing_translations:
            counter += 1
            translated_text = await translator.translate(
                target_language=translate_language, text=value
            )
            dictionary[key] = translated_text
            if print_logs:
                print(f"Переведено {counter} из {number_of_values}: {key}")

    if print_logs:
        print(f"Стоимость перевода: {translator.get_usage_price()} USD")
        print(f"Общее время перевода: {time.time() - t1} секунд")

    # Обновление существующего файла перевода
    existing_translations.update(dictionary)
    parser.load_to_file(existing_translations, file_path=translated_dict_path)


async def main():
    max_threads = 10  # число потоков
    source_language_code = "ru"
    # source_file_path = "messages/ru.py"  # Если скрипт запущен из папки lang, этот путь корректен.
    source_file_path = os.path.join(os.getcwd(), "messages", "ru.py")
    print(f"Исходный файл переводов: {source_file_path}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = []
        for language_name, language_code in languages.items():
            if language_code != source_language_code:
                translated_dict_path = os.path.join(os.getcwd(), "messages", f"{language_code}.py")
                futures.append(
                    executor.submit(
                        asyncio.run, 
                        translate_dictionary(
                            translated_dict_path=translated_dict_path,
                            translate_language=language_name,
                            main_dict_path=source_file_path,
                            print_logs=True,
                            use_ignored_keys=False
                        )
                    )
                )
        for future in concurrent.futures.as_completed(futures):
            future.result()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    asyncio.run(main())

