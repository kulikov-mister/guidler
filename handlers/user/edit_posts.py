# handlers/user/edit_posts.py
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from Filter.Filter import IsNotCommand
from database.get_to_db import get_post_and_category_posts_by_id, get_posts_by_category_id
from database.update_to_db import update_post
from database.delete_from_db import delete_post_by_id
from loader import dp
from lang.get_message import get_message, extract_language
from states.user_states import EditPost
from keyboards.inline.inlline_back import approve_delete_keyboard, return_keyboard
from utils.telegraph_utils import create_telegraph_account, create_telegraph_page
from utils.text_cleaner import clean_text_for_telegraph

router = Router()
dp.include_router(router)


# кнопка редактирования поста
@router.callback_query(F.data.startswith('editPost:'))
async def edit_data_post(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    parts = call.data.split(":")
    action = parts[1]
    post_id = int(parts[2])
    await state.update_data(editing_post_id=post_id)
    
    if action == "name":
        await call.message.delete()
        await call.message.answer(get_message(lang, "prompt_new_name"))
        await state.set_state(EditPost.editing_name)

    elif action == "desc":
        await call.message.delete()
        await call.message.answer(get_message(lang, "prompt_new_desc"))
        await state.set_state(EditPost.editing_desc)

    elif action == "media":
        await call.message.delete()
        await call.message.answer(get_message(lang, "prompt_new_media"))
        await state.set_state(EditPost.editing_media)

    elif action == "delete":
        msg = get_message(lang, "post_capcha_deleted")
        inline_kb = approve_delete_keyboard("okDelete", post_id, lang)
        await call.message.delete()
        await call.message.answer(msg, reply_markup=inline_kb)
        await state.set_state(EditPost.deleting_post)

# подтверждение удаления
@router.callback_query(F.data.startswith('okDelete:'))
async def delete_post_collback(call: CallbackQuery, state: FSMContext):
    lang = extract_language(call)
    post_id = int(call.data.split(":")[1])
    await delete_post_by_id(post_id)
    await call.message.edit_text(get_message(lang, "post_deleted"), reply_markup=None)
    await state.clear()

# редактирование названия faq
@router.message(IsNotCommand(), EditPost.editing_name)
async def process_name_editing(message: Message, state: FSMContext):
    lang = extract_language(message)
    title = message.text
    if len(title) < 50:
        new_name = message.html_text
        state_data = await state.get_data()
        post_id = state_data.get('editing_post_id')
        await update_post(post_id, {"name": new_name})
        category_id = state_data.get('category_id')
        user_posts = await get_posts_by_category_id(category_id)
        await state.update_data(posts=user_posts)
        inline_kb = return_keyboard(post_id, lang)
        await message.answer(get_message(lang, "post_name_updated"), reply_markup=inline_kb)
        
    else:
        await message.answer(get_message(lang, "post_name_too_long"))

# редактирование текста faq
@router.message(IsNotCommand(), EditPost.editing_desc)
async def process_desc_editing(message: Message, state: FSMContext):
    lang = extract_language(message)
    new_desc_text = message.text
    new_desc_html = message.html_text
    state_data = await state.get_data()
    post_id = state_data.get('editing_post_id')

    # если текст длинный то сохраняем его в телеграф
    if len(new_desc_text)>700:
        post, _ = await get_post_and_category_posts_by_id(post_id)
        faq_name = post.name
        cleaned_text = clean_text_for_telegraph(new_desc_html)
        telegraph = await create_telegraph_account()
        page = await create_telegraph_page(telegraph, faq_name, cleaned_text)
        post_url = page.url
        new_desc_html = f"<a href='{post_url}'>{faq_name}</a>"    

    await update_post(post_id, {"text": new_desc_html})
    category_id = state_data.get('category_id')
    user_posts = await get_posts_by_category_id(category_id)
    await state.update_data(posts=user_posts)

    inline_kb = return_keyboard(post_id, lang)
    await message.answer(get_message(lang, "post_desc_updated"), reply_markup=inline_kb)

# редактирование контента faq
@router.message(F.content_type.in_({'photo', 'audio', 'video', 'animation', 'document'}), EditPost.editing_media)
async def process_pic_editing(message: Message, state: FSMContext):
    lang = extract_language(message)
    new_pic_file_id = message.photo[-1].file_id if message.content_type == 'photo' else \
                      message.audio.file_id if message.content_type == 'audio' else \
                      message.video.file_id if message.content_type == 'video' else \
                      message.animation.file_id if message.content_type == 'animation' else \
                      message.document.file_id if message.content_type == 'document' else None
    
    if new_pic_file_id:
        state_data = await state.get_data()
        post_id = state_data.get['editing_post_id']
        await update_post(post_id, {"pic": new_pic_file_id})
        
        inline_kb = return_keyboard(post_id, lang)
        await message.answer(get_message(lang, "post_media_updated"), reply_markup=inline_kb)
    else:
        await message.answer(get_message(lang, "pls_send_img"))