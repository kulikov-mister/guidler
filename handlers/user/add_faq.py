# handlers/user/add_faq.py
import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from Filter.Filter import IsNotCommand
from database.add_to_db import add_post
from database.get_to_db import (
    get_user, get_categories_with_cache, get_user_instructions_with_cache, get_posts_by_user_id
    )
from loader import dp
from lang.get_message import get_message, extract_language
from states.user_states import CreatePost, MyPosts
from keyboards.inline.categories_keyboards import instructions_keyboard, categories_keyboard
from keyboards.inline_builder import get_paginated_posts_keyboard
from utils.code_generator import generate_random_string_async_lower
from utils.telegraph_utils import create_telegraph_account, create_telegraph_page
from utils.text_cleaner import clean_text_for_telegraph
from .publish import linksPost_creator, chunk_posts


router = Router()
dp.include_router(router)
    

# Команда начала добавления FAQ
@router.message(Command('add_faq'))
async def add_faq_command(message: Message, state: FSMContext):
    lang = extract_language(message)
    user_id = message.from_user.id
    user_data = await get_user(user_id)

    if user_data['type'] in ["creator", "admin" , "user", "pro"]:
        instructions = await get_user_instructions_with_cache(user_id)

        if not instructions:
            await message.answer(get_message(lang, "not_instruction_default"))
            return
        
        inline_kb = instructions_keyboard(instructions, "chooseInstruction", "mainstart_help", 1)
        await message.answer(get_message(lang, "micro_plan_faq"))
        await asyncio.sleep(2)

        await message.answer(
            get_message(lang, "choose_instruction_for_faq"),
            reply_markup=inline_kb
            )
        await state.set_state(CreatePost.InstructionId)
        
    elif not user_data:
        await message.answer(get_message(lang, "registration_required_message"))
        return


# Пользователь выбирает инструкцию
@router.callback_query(F.data.startswith('chooseInstruction:'), CreatePost.InstructionId)
async def select_instruction(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    instruction_id = call.data.split(":")[1]

    if instruction_id:
        await state.update_data(instruction_id=instruction_id)
        categories = await get_categories_with_cache(instruction_id)
        if categories:
            inline_kb = categories_keyboard(categories, "chooseCategory", "back_to_instruction", 1)
            await call.message.edit_text(get_message(lang, "choose_category_for_faq"), reply_markup=inline_kb)
            await state.set_state(CreatePost.CategoryId)
        else:
            await call.answer(get_message(lang, "not_categories_for_faq"), show_alert=1)


# хендлер на переключение страниц
@router.callback_query(F.data.startswith("page:"), StateFilter(CreatePost.InstructionId, CreatePost.CategoryId, MyPosts.AllPosts, MyPosts.CategoryId))
async def query_page_navigation(call: CallbackQuery, state: FSMContext):
    print(call.data)
    lang = extract_language(call)
    user_id = call.from_user.id
    parts = call.data.split(":")
    cb_prefix = parts[1]
    page = int(parts[-1])
    state_data = await state.get_data()
    current_state = await state.get_state()

    if cb_prefix == "chooseInstruction":
        instructions = await get_user_instructions_with_cache(user_id)
        msg = call.message.html_text
        inline_kb = instructions_keyboard(instructions, "chooseInstruction", "mainstart_help", page)
    
    elif cb_prefix == "chooseCategory":
        instruction_id = state_data.get('instruction_id')
        if instruction_id:
            categories = await get_categories_with_cache(instruction_id)
            msg = call.message.html_text
            prefix = "back_to_instruction"
            
            if current_state == "MyPosts:CategoryId":
                prefix = "my_posts"
            inline_kb = categories_keyboard(categories, "chooseCategory", prefix, page)

    elif cb_prefix == "all_posts":
        user_posts = state_data.get("posts")

        if not user_posts:
            user_posts = await get_posts_by_user_id(user_id)

        chunked_posts = list(chunk_posts(user_posts, 10))
        msg = await linksPost_creator(chunked_posts[page], "all_posts", None, None, None, page*10)
        inline_kb = get_paginated_posts_keyboard(len(chunked_posts), page, "delete", "all_posts")


    if inline_kb:
        await call.answer(get_message(lang, "page_alert") + f" {page}")
        await call.message.edit_text(text=msg, reply_markup=inline_kb)
    else:
        await call.answer(get_message(lang, "navigation_error"))
    return


# Пользователь выбирает категорию
@router.callback_query(F.data.startswith('chooseCategory:'), CreatePost.CategoryId)
async def select_category(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    category_id = call.data.split(':')[1]
    user_id = call.from_user.id

    user_data = await get_user(user_id)
    if user_data['type'] in ["creator", "admin" , "user", "pro"]:


        await state.update_data(category_id=category_id)
        await call.message.edit_text(get_message(lang, "enter_faq_name"),
            reply_markup=None,
            )
        await state.set_state(CreatePost.FAQName)


# Пользователь вводит название FAQ
@router.message(IsNotCommand(), CreatePost.FAQName)
async def enter_faq_name(message: Message, state: FSMContext):
    lang = extract_language(message)
    faq_name = message.text
    if len(faq_name) > 30:
        await message.answer(get_message(lang, "category_name_too_long"))
        return
    
    await state.update_data(name=faq_name)
    await message.answer(get_message(lang, "enter_faq_content"))
    await state.set_state(CreatePost.FAQContent)


# Пользователь вводит содержимое FAQ (текст или медиа)
@router.message(F.content_type.in_(['text', 'photo', 'video', 'animation', 'document']), CreatePost.FAQContent)
async def enter_faq_content(message: Message, state: FSMContext):
    lang = extract_language(message)
    content_type = message.content_type
    text = message.text
    
    content = None if content_type == 'text' else message.photo[-1].file_id if content_type == 'photo' else message.video.file_id if content_type == 'video' else message.document.file_id
    html_text = message.html_text if content_type == 'text' else message.html_text

    user_id = message.from_user.id
    state_data = await state.get_data()
    category_id = state_data.get("category_id")
    faq_name = state_data.get("name")
    code = await generate_random_string_async_lower(16)

    if message.text:
        if len(text) > 700:
            cleaned_text = clean_text_for_telegraph(html_text)
            telegraph = await create_telegraph_account()
            page = await create_telegraph_page(telegraph, faq_name, cleaned_text)
            post_url = page.url
            html_text = f"<a href='{post_url}'>{faq_name}</a>"
        else:
            html_text


    await add_post(user_id, faq_name, content_type, html_text, content, category_id, code)
    await message.answer(get_message(lang, "faq_added_successfully"))
    await asyncio.sleep(1)
    await message.answer(get_message(lang, "enter_faq_name"))
    await state.set_state(CreatePost.FAQName)
