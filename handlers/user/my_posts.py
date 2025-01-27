# handlers/user/my_posts.py
import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from database.get_to_db import (
    get_posts_by_user_id, get_user, get_user_instructions_with_cache, get_categories_with_cache, get_instruction_by_id,
    get_posts_by_category_id
)
from loader import dp
from lang.get_message import get_message, extract_language
from states.user_states import MyPosts
from keyboards.inline.categories_keyboards import (
    instructions_keyboard, categories_keyboard, posts_view_keyboard
    )
from keyboards.inline_builder import get_paginated_posts_keyboard
from utils.cache_utils import CacheManager
from config_data.config import ADMIN_IDS
from .publish import linksPost_creator, chunk_posts
from .viewer import send_post_content


router = Router()
dp.include_router(router)


# команда my_posts
@router.message(Command('my_posts'))
async def my_posts_command(message: Message, state: FSMContext):
    lang= extract_language(message)
    user_id = message.from_user.id
    user_data = await get_user(user_id)

    if user_data['type'] in ["creator", "admin" , "user", "pro"]:
        instructions = await get_user_instructions_with_cache(user_id)

        if not instructions:
            await message.answer(get_message(lang, "not_instruction_default"))
            return
        
        inline_kb = instructions_keyboard(instructions, "chooseInstruction", "help", 1)
        await message.answer(get_message(lang, "micro_plan_my_posts"))
        await asyncio.sleep(1)

        await message.answer(
            get_message(lang, "choose_instruction"),
            reply_markup=inline_kb
            )
        await state.set_state(MyPosts.InstructionId)
        
    elif not user_data:
        await message.answer(get_message(lang, "registration_required_message"))
        return


# колбек my_posts
@router.callback_query(F.data ==('my_posts'))
async def my_posts_collback(call: CallbackQuery, state: FSMContext):
    lang= extract_language(call)
    user_id = call.from_user.id

    await call.answer("✅")
    instructions = await get_user_instructions_with_cache(user_id)
    if not instructions:
        await call.message.edit_text(get_message(lang, "not_instruction_default"))
        return
    
    inline_kb = instructions_keyboard(instructions, "chooseInstruction", "help", 1)
    await call.message.edit_text(get_message(
        lang, "choose_instruction"), reply_markup=inline_kb
        )
    await state.set_state(MyPosts.InstructionId)



# Пользователь выбирает инструкцию
@router.callback_query(F.data.startswith('chooseInstruction:'), StateFilter(MyPosts.InstructionId, MyPosts.CategoryId, MyPosts.MyPosts))
async def select_instruction(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    instruction_id = call.data.split(":")[1]

    if instruction_id:
        instruction_data =  await get_instruction_by_id(instruction_id)
        await state.update_data(instruction_id=instruction_id, group_id=instruction_data.group_id)
        categories = await get_categories_with_cache(instruction_id)
        if categories:
            inline_kb = categories_keyboard(categories, "chooseCategory", "my_posts", 1)
            await call.message.edit_text(get_message(lang, "choose_category"), reply_markup=inline_kb)
            await call.answer("✅")                
            await state.set_state(MyPosts.CategoryId)
        else:
            await call.answer(get_message(lang, "not_categories_for_faq"), show_alert=1)



# Пользователь выбирает категорию
@router.callback_query(F.data.startswith('chooseCategory:'), MyPosts.CategoryId)
async def select_category(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    category_id = call.data.split(':')[1]
    await state.update_data(category_id=category_id)

    user_posts = await get_posts_by_category_id(category_id)
    if user_posts:
        formatted_posts = [{'id': post.id, 'name': post.name, 'code': post.code} for post in user_posts]
        active_post = user_posts[0]
        inline_kb = posts_view_keyboard(formatted_posts, active_post.id, "post_view", "delete", r="my_posts")
        await state.update_data(posts=user_posts, active_post_id=active_post.id)
        await call.message.delete()
        await send_post_content(call, active_post, inline_kb)
        await state.set_state(MyPosts.MyPosts)
        await call.answer("✅")
    
    else:
        await call.message.edit_text(get_message(lang, "not_posts_in_db"), reply_markup=None)
        await call.answer()




# команда all_posts
@router.message(Command('all_posts'))
async def all_posts_command(message: Message, state: FSMContext):
    lang= extract_language(Message)
    user_id = message.from_user.id

    user_data = await get_user(user_id)
    if user_data['type'] in ["creator", "admin" , "user", "pro"]:

        user_posts = await get_posts_by_user_id(user_id)    
        if user_posts:
            chunked_posts = list(chunk_posts(user_posts, 10))
            await state.update_data(posts=user_posts)
            postsText = await linksPost_creator(chunked_posts[0], "all_posts", None, None, None, 0)
            inline_kb = get_paginated_posts_keyboard(len(chunked_posts), 0, "delete", "all_posts")
            await message.answer(postsText, reply_markup=inline_kb)
            await state.set_state(MyPosts.AllPosts)
            
    elif not user_data:
        await message.answer(get_message(lang, "registration_required_message"))
        return
