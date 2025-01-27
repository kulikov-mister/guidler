# states/admin_states.py
from aiogram.filters.state import StatesGroup, State

class update_state(StatesGroup):
    SendUpd = State()
