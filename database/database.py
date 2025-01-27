# database/database.py
import asyncio
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import relationship, backref
from config_data.config import SQLALCHEMY_DATABASE_URL

async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)


# Создание экземпляра engine для подключения к базе данных
async def async_create_table(table):
    async with async_engine.begin() as conn:
        await conn.run_sync(table.create, checkfirst=True)


# Базовый класс для всех моделей
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    type = Column(String)

class Instruction(Base):
    __tablename__ = 'instruction'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    title = Column(String)
    group_id = Column(String)
    group_name = Column(String)
    image_url = Column(String)
    language = Column(String)
    code = Column(String(8), unique=True)
    categories = relationship('Category', backref='instruction')
    
class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    instruction_id = Column(Integer, ForeignKey('instruction.id'))
    name = Column(String)
    post_order = Column(String, nullable=True)
    code = Column(String(12), unique=True)
    posts = relationship('Posts', backref='category')

    def as_dict(self):
        return {
            "id": self.id,
            "instruction_id": self.instruction_id,
            "name": self.name,
            "post_order": self.post_order,
            "code": self.code,
        }

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.user_id'))
    name = Column(String)
    type = Column(String)
    text = Column(String)
    file_id = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    code = Column(String(16), unique=True)

    def as_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "type": self.type,
            "text": self.text,
            "file_id": self.file_id,
            "category_id": self.category_id,
            "code": self.code,
            # Сюда можно добавить любые дополнительные поля
        }


class PublishedPage(Base):
    __tablename__ = 'published_pages'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    instruction_id = Column(Integer, ForeignKey('instruction.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    data = Column(Text)
    page = Column(Integer)

    __table_args__ = (
        Index('ix_instruction_category', 'instruction_id', 'category_id', unique=False),
    )
    
    def as_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "instruction_id": self.instruction_id,
            "category_id": self.category_id,
            "data": self.data,
            "page": self.page,
            # Сюда можно добавить любые дополнительные поля
        }



async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



asyncio.run(async_main())


