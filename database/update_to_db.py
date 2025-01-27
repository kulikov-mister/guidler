# database/update_to_db.py
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import async_engine, User, Instruction, Category, Posts, PublishedPage

AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

# функция для обновления постов
async def update_post(post_id, update_fields):
    async with AsyncSessionLocal() as session:
        query = select(Posts).where(Posts.id == post_id)
        result = await session.execute(query)
        post = result.scalars().first()

        if post:
            for field, value in update_fields.items():
                if hasattr(post, field) and field != 'id':
                    setattr(post, field, value)

            await session.commit()
            return post
        else:
            return None
    
    
# функция для обновления категории
async def update_category(category_id, update_fields):
    async with AsyncSessionLocal() as session:
        query = select(Category).where(Category.id == category_id)
        result = await session.execute(query)
        category = result.scalars().first()

        if category:
            for field, value in update_fields.items():
                if hasattr(category, field) and field != 'id':
                    setattr(category, field, value)

            await session.commit()
            return category
        else:
            return None
    
    
