# database/get_to_db.py
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.database import async_engine, User, Category, Instruction, Posts, PublishedPage
from utils.cache_utils import CacheManager


# Асинхронный движок и создание сессии
AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


# Создаем экземпляр CacheManager
cache_manager = CacheManager()


# Пример функции чтения данных из базы данных
async def get_user(user_id):
    user_data = await cache_manager.get_data(user_id)
    if user_data is not None:
        return user_data

    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User).where(User.user_id == user_id))
        user = result.scalars().first()

        if user:
            user_data = {
                "user_id": user.user_id,
                "name": user.name,
                "type": user.type,
            }
            await cache_manager.set_data(user_id, user_data)

    return user_data if user_data else None




# Пример функции get_categories_with_cache
async def get_categories_with_cache(instruction_id):
    cached_data = await cache_manager.get_data(f"instruction_{instruction_id}_categories")
    if cached_data:
        return cached_data

    async with AsyncSessionLocal() as session:
        categories = await session.execute(
            select(Category).where(Category.instruction_id == instruction_id)
        )
        categories = categories.scalars().all()

    categories_data = [{
        "id": category.id,
        "name": category.name,
        "post_order": category.post_order,
        "instruction_id": category.instruction_id
    } for category in categories]

    await cache_manager.set_data(f"instruction_{instruction_id}_categories", categories_data)
    return categories_data


# Пример функции check_instruction
async def check_instruction(user_id, title, group_id):
    async with AsyncSessionLocal() as session:
        instruction_exists = await session.execute(
            select(Instruction).where(
                Instruction.user_id == user_id, 
                Instruction.title == title, 
                Instruction.group_id == group_id
            )
        )
        instruction_exists = instruction_exists.scalar_one_or_none()
        return instruction_exists is not None


# Пример функции get_user_instructions
async def get_user_instructions(user_id):
    async with AsyncSessionLocal() as session:
        instructions = await session.execute(
            select(Instruction).where(Instruction.user_id == user_id)
        )
        instructions = instructions.scalars().all()
        return instructions


# Функция get_user_instructions_with_cache
async def get_user_instructions_with_cache(user_id):
    user_data = await cache_manager.get_data(user_id)
    if user_data and "instructions" in user_data:
        return user_data["instructions"]

    async with AsyncSessionLocal() as session:
        instructions = await session.execute(
            select(Instruction).where(Instruction.user_id == user_id)
        )
        instructions = instructions.scalars().all()

    instructions_data = [{ 
        "id": instruction.id, 
        "title": instruction.title, 
        "group_id": instruction.group_id, 
        "group_name": instruction.group_name,
        "image_url": instruction.image_url, 
        "language": instruction.language,
    } for instruction in instructions]

    if user_data is None:
        user_data = {}

    user_data["instructions"] = instructions_data
    await cache_manager.set_data(user_id, user_data)

    return instructions_data


# уникальные чаты пользователя
async def get_user_unique_chats(user_id):
    async with AsyncSessionLocal() as session:
        instructions = await session.execute(
            select(Instruction).where(Instruction.user_id == user_id)
        )
        instructions = instructions.scalars().all()

    unique_chats = {}
    for instruction in instructions:
        unique_chats[instruction.group_id] = (
            instruction.group_name, 
            instruction.title, 
            instruction.image_url
        )
    return unique_chats


# уникальные чаты пользователя с кешем
async def get_user_unique_chats_with_cache(user_id):
    user_data = await cache_manager.get_data(user_id)
    if user_data and "unique_chats" in user_data:
        return user_data["unique_chats"]

    unique_chats = await get_user_unique_chats(user_id)
    if user_data is None:
        user_data = {}

    user_data["unique_chats"] = unique_chats
    await cache_manager.set_data(user_id, user_data)

    return unique_chats


# инструкции по group_id
async def get_instructions_by_group_id(group_id):
    async with AsyncSessionLocal() as session:
        instructions = await session.execute(
            select(Instruction).where(Instruction.group_id == group_id)
        )
        return instructions.scalars().all()


# инструкции по id
async def get_instruction_by_id(instruction_id):
    async with AsyncSessionLocal() as session:
        instruction = await session.get(Instruction, instruction_id)
        return instruction


# Категории по id
async def get_category_by_id(category_id):
    async with AsyncSessionLocal() as session:
        category = await session.get(Category, category_id)
        return category


# Посты по category_id
async def get_posts_by_category_id(category_id):
    async with AsyncSessionLocal() as session:
        posts = await session.execute(
            select(Posts).where(Posts.category_id == category_id)
        )
        return posts.scalars().all()


# Посты по user_id
async def get_posts_by_user_id(user_id):
    async with AsyncSessionLocal() as session:
        posts = await session.execute(
            select(Posts).where(Posts.user_id == user_id)
        )
        return posts.scalars().all()


# Опубликованные страницы по user_id
async def get_published_pages_by_user_id(user_id):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(PublishedPage).where(PublishedPage.user_id == user_id)
        )
        published_pages = result.scalars().all()
        return published_pages


# Опубликованные страницы пользователя в категории
async def get_published_pages_by_user_and_category(user_id, category_id):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(PublishedPage).where(
                (PublishedPage.user_id == user_id) & 
                (PublishedPage.category_id == category_id)
            )
        )
        published_pages = result.scalars().all()
        return published_pages


# Информация о посте и категории по коду поста
async def get_post_and_category_by_code(code):
    async with AsyncSessionLocal() as session:
        post = await session.execute(
            select(Posts).where(Posts.code == code)
        )
        post = post.scalar_one_or_none()

        if post:
            category = await session.get(Category, post.category_id)
            return post, category

        return None, None
    
    
# Получение поста и всех постов его категории по ID поста
async def get_post_and_category_posts_by_id(post_id):
    async with AsyncSessionLocal() as session:
        post = await session.get(Posts, post_id)

        if post:
            posts_query = await session.execute(
                select(Posts).where(Posts.category_id == post.category_id)
            )
            posts_list = posts_query.scalars().all()
            posts_dicts = [p.as_dict() for p in posts_list]
            return post, posts_dicts

        return None, None



# Опубликованные посты по id
async def get_published_page_by_id(id):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(PublishedPage).where(PublishedPage.id == id)
        )
        published_page = result.scalar_one_or_none()

        if published_page:
            return published_page.as_dict()
        return None

# Опубликованные посты по id и страницам
async def get_published_page_by_id_and_page(id, page):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(PublishedPage).where(
                (PublishedPage.id == id) & (PublishedPage.page == page)
            )
        )
        published_page = result.scalar_one_or_none()

        if published_page:
            return published_page.as_dict()
        return None


# Информация о посте и категории по коду поста с кэшированием
async def get_post_and_category_by_code_with_cache(code):
    cached_data = await cache_manager.get_data(f"post_{code}")
    if cached_data:
        return cached_data

    async with AsyncSessionLocal() as session:
        post = await session.execute(
            select(Posts).where(Posts.code == code)
        )
        post = post.scalar_one_or_none()

        if post:
            category = await session.get(Category, post.category_id)
            if category:
                # Преобразуем объекты в словари для сериализации
                post_data = post.as_dict()
                category_data = category.as_dict()

                # Сохраняем данные в кэш
                cache_data = {"post": post_data, "category": category_data}
                await cache_manager.set_data(f"post_{code}", cache_data)

                return cache_data

    return None

