# states/user_states.py
from aiogram.filters.state import StatesGroup, State



class UserRegistrationState(StatesGroup):
    name = State()
    phone = State()


class StartState(StatesGroup):
    Role = State()


class CreateInstruction(StatesGroup):
    GroupId = State()
    Name = State()
    Language = State()

class CreateCategory(StatesGroup):
    InstructionId = State()
    Name = State()
    Language = State()


class CreatePost(StatesGroup):
    InstructionId = State()
    CategoryId = State()
    FAQName = State()
    FAQContent = State()


class Publish(StatesGroup):
    InstructionId = State()
    InstructionIdAll = State()
    CategoryId = State()
    CategoryIdAll = State()
    SentCheck = State()
    Approve = State()
    ChoosePostsOrder = State()


class Viewer(StatesGroup):
    SortedPosts = State()
    AllPosts = State()
    Instructions = State()
    
    
class MyPosts(StatesGroup):
    InstructionId = State()
    CategoryId = State()
    PublishedPosts = State()
    MyPosts = State()
    AllPosts = State()
    Instructions = State()
    Categories = State()


class EditPost(StatesGroup):
    editing_name = State()
    editing_desc = State()
    editing_media = State()
    deleting_post = State()
    
class EditCategory(StatesGroup):
    editing_name = State()
    deleting_category = State()
    