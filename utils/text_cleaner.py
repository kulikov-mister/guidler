# utils/text_cleaner.py
import re

def clean_text_for_telegraph(text):
    text = re.sub(r'<tg-emoji[^>]*?>(.*?)</tg-emoji>', r'\1', text)

    return text