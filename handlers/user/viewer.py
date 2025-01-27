# handlers/user/publicate.py
import re, json
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, CommandObject, StateFilter
from aiogram.fsm.context import FSMContext
from database.get_to_db import (
    get_posts_by_category_id, get_post_and_category_by_code, get_published_page_by_id
)
from loader import dp
from lang.get_message import get_message, extract_language
from keyboards.inline.categories_keyboards import posts_view_keyboard
from states.user_states import Viewer, MyPosts, EditPost


router = Router()
dp.include_router(router)


# Функция для сортировки постов по выбранному порядку
def sort_posts_by_order(posts, selected_order):
    sorted_posts = []
    # Ищем посты в заданном порядке и добавляем их в новый список
    for post_id in selected_order:
        for post in posts:
            if post.id == post_id:
                sorted_posts.append(post)
                break
    return sorted_posts


# хендлер для чтения инструкций через диплинк
@router.message(CommandStart(deep_link=True, magic=F.args.len().in_([8, 12, 16])))
async def deeplinks_faq_viewer(message: Message, command: CommandObject, state: FSMContext):
    lang = extract_language(message)
    code = command.args

    if len(code) == 8: # инструкция
        print(code)
    
    
    elif len(code) == 12: # категория
        print(code)
    
    
    elif len(code) == 16:  # faq-пост
        active_post, category = await get_post_and_category_by_code(code)
        posts = await get_posts_by_category_id(category.id)

        if active_post and posts:
            formatted_posts = [{'id': p.id, 'name': p.name} for p in posts]
            inline_kb = posts_view_keyboard(formatted_posts, active_post.id, "post_view", "delete")
            await send_post_content(message, active_post, inline_kb)
            await state.set_state(Viewer.AllPosts)
            await state.update_data(category_id=active_post.category_id, active_post_id=active_post.id, posts=posts)


# просмотр отсортированных постов пользователя
@router.message( CommandStart(deep_link=True, magic=(F.args.regexp(r"^\d+_[a-z\d]+$"))) )
async def handle_deep_link(message: Message, command: CommandObject, state: FSMContext):
    cod = command.args
    id, code = cod.split("_")
    state_data = await state.get_data()
    if id.isdigit():
        published_post = await get_published_page_by_id(id)
    elif cod.startswith('all_posts_'):
         _, _, code = cod.split("_")
    
    published_data = json.loads(published_post['data'])
    category_id = published_post['category_id']
    posts = state_data.get("posts")
    active_post, category = await get_post_and_category_by_code(code)

    if not posts and id.isdigit():
        all_posts = await get_posts_by_category_id(category.id)
        sorted_posts = sort_posts_by_order(all_posts, published_data)
        await state.update_data(category_id=category_id, posts=sorted_posts)
        posts = state_data.get("posts", sorted_posts)


    if active_post and posts:
        await state.set_state(Viewer.SortedPosts)
        formatted_posts = [{'id': p.id, 'name': p.name, 'code': p.code} for p in posts]
        inline_kb = posts_view_keyboard(formatted_posts, active_post.id, "post_view", "delete", cod)

        await send_post_content(message, active_post, inline_kb)


# просмотр всех постов пользователя
@router.message( CommandStart(deep_link=True, magic=F.args.regexp(r"^all_posts_[a-z\d]+$")) )
async def handle_deep_link(message: Message, command: CommandObject, state: FSMContext):
    lang= extract_language(message)
    cod = command.args
    code = cod.split("_")[-1]
    state_data = await state.get_data()

    active_post, category = await get_post_and_category_by_code(code)
    if not category or not active_post:
        await message.answer(get_message(lang, "not_post_in_db"))
        return
    all_posts = await get_posts_by_category_id(category.id)
    await state.update_data(category_id=category.id, posts=all_posts)
    posts = state_data.get("posts", all_posts)


    if active_post and posts:
        await state.set_state(MyPosts.AllPosts)
        formatted_posts = [{'id': p.id, 'name': p.name, 'code': p.code} for p in posts]
        inline_kb = posts_view_keyboard(formatted_posts, active_post.id, "post_view", "delete", "my_posts", "my_posts")
        await send_post_content(message, active_post, inline_kb)


# Хендлер для переключения постов и отображения содержимого поста
@router.callback_query(F.data.startswith("post_view:"), 
    StateFilter(Viewer.AllPosts, Viewer.SortedPosts, MyPosts.AllPosts, EditPost.deleting_post, EditPost.editing_name,
                EditPost.editing_desc, EditPost.editing_media, MyPosts.MyPosts))
async def post_navigation_handler(call: CallbackQuery, state: FSMContext):
    parts = call.data.split(":")
    post_id = int(parts[1])
    cod = parts[2] if len(parts) > 2 else None
    state_data = await state.get_data()
    posts = state_data.get("posts")
    if cod and "_" in cod and cod.startswith('all_posts_'):
        id, code = cod.split("_")
        published_post = await get_published_page_by_id(id)
        published_data = json.loads(published_post['data'])
        category_id = published_post['category_id']
        active_post, category = await get_post_and_category_by_code(code)
        if category_id is None:
            category_id = category.id
        all_posts = await get_posts_by_category_id(category_id)
        sorted_posts = sort_posts_by_order(all_posts, published_data)
        await state.update_data(posts=sorted_posts)

    if posts is None:
        # Обрабатываем ситуацию, когда постов не найдено
        return
    
    else:
        active_post = next((p for p in posts if p.id == post_id), None)

    if active_post:
        await call.answer("✅")        
        await call.message.delete()

        formatted_posts = [{'id': p.id, 'name': p.name, 'code': p.code} for p in posts]
        prefix = cod if cod else None
        current_state = await state.get_state()
        if current_state in ("EditPost:deleting_post", "EditPost:editing_name", "EditPost:editing_desc", "EditPost:editing_media"):
            await state.set_state(MyPosts.AllPosts)
        r = "my_posts" if current_state in ("MyPosts:AllPosts", "EditPost:deleting_post", "EditPost:editing_name", "EditPost:editing_desc", "MyPosts:MyPosts") else None
        inline_kb = posts_view_keyboard(formatted_posts, post_id, "post_view", "delete", prefix=prefix, r=r)
        await send_post_content(call, active_post, inline_kb)
        await state.update_data(active_post_id=post_id)


# функция подбора ответа на основании типа поста
async def send_post_content(interaction, post, inline_kb):
    send_method = None

    # Определяем метод отправки в зависимости от типа взаимодействия
    if isinstance(interaction, Message):
        send_method = interaction
    elif isinstance(interaction, CallbackQuery):
        send_method = interaction.message

    # Если метод отправки определен, отправляем содержимое поста
    if send_method:
        if post.type == 'text':
            await send_method.answer(text=post.text, reply_markup=inline_kb, parse_mode="HTML")

        elif post.type == 'photo':
            await send_method.answer_photo(post.file_id, caption=post.text, reply_markup=inline_kb, parse_mode="HTML")

        elif post.type == 'video':
            await send_method.answer_video(post.file_id, caption=post.text, reply_markup=inline_kb, parse_mode="HTML")

        elif post.type == 'audio':
            await send_method.answer_audio(post.file_id, caption=post.text, reply_markup=inline_kb, parse_mode="HTML")

        elif post.type == 'animation':
            await send_method.answer_animation(post.file_id, caption=post.text, reply_markup=inline_kb, parse_mode="HTML")

        elif post.type == 'document':
            await send_method.answer_document(post.file_id, caption=post.text, reply_markup=inline_kb, parse_mode="HTML")