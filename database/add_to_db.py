# database/add_to_db.py
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import async_engine, User, Instruction, Category, Posts, PublishedPage

AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)



async def add_user(user_id, name, user_type):
    async with AsyncSessionLocal() as session:
        new_user = User(user_id=user_id, name=name, type=user_type)
        session.add(new_user)
        await session.commit()
        return new_user

async def add_instruction(user_id, title, group_id, group_name, image_url, language, code):
    async with AsyncSessionLocal() as session:
        new_instruction = Instruction(
            user_id=user_id, title=title, group_id=group_id, 
            group_name=group_name, image_url=image_url, language=language, code=code
        )
        session.add(new_instruction)
        await session.commit()
        return new_instruction

async def add_category(instruction_id, name, code):
    async with AsyncSessionLocal() as session:
        new_category = Category(
            instruction_id=instruction_id, name=name, 
            code=code
        )
        session.add(new_category)
        await session.commit()
        return new_category

async def add_post(user_id, name, post_type, text, file_id, category_id, code):
    async with AsyncSessionLocal() as session:
        new_post = Posts(
            user_id=user_id, name=name, type=post_type, 
            text=text, file_id=file_id, category_id=category_id, code=code
        )
        session.add(new_post)
        await session.commit()
        return new_post

async def add_published_page(user_id, instruction_id, category_id, data, page=1):
    async with AsyncSessionLocal() as session:
        new_published_page = PublishedPage(
            user_id=user_id,
            instruction_id=instruction_id,
            category_id=category_id,
            data=json.dumps(data),
            page=page
        )
        session.add(new_published_page)
        await session.commit()
        return new_published_page.id
