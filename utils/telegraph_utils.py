# utils/telegraph_utils.py
from aiograph import Telegraph
from config_data.config import PROXY_URL

async def create_telegraph_account():
    telegraph = Telegraph(proxy=PROXY_URL)
    await telegraph.create_account('Guidler Bot', "Guidler", "https://t.me/guidler_bot")
    return telegraph

async def create_telegraph_page(telegraph, title, html_content):
    page = await telegraph.create_page(title, html_content, author_name="Guidler", author_url="https://t.me/guidler_bot")
    await telegraph.close()
    return page


async def update_telegraph_page(telegraph, title, html_content):
    page = await telegraph.update_page(title, html_content, author_name="Guidler", author_url="https://t.me/guidler_bot")
    await telegraph.close()
    return page