# database/delete_from_db.py
from sqlalchemy import delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.database import async_engine, User, Category, Instruction, Posts, PublishedPage


# Асинхронный движок и создание сессии
AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


# Функция удаления поста по ID
async def delete_post_by_id(post_id):
    async with AsyncSessionLocal() as session:
        delete_query = delete(Posts).where(Posts.id == post_id)
        await session.execute(delete_query)
        await session.commit()
        
