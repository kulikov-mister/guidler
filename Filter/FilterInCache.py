# Filter/FilterInCache.py
from utils.cache_utils import CacheManager
from aiogram.types import Message, ChatMemberUpdated
from aiogram.filters import BaseFilter



cache_manager = CacheManager()


# проверка данных в кеше
class CachedDataFilter(BaseFilter):
    key = 'has_cached_data'

    def __init__(self, has_cached_data, cache_manager: CacheManager):
        self.has_cached_data = has_cached_data
        self.cache_manager = cache_manager

    async def check(self, message: Message) -> bool:
        user_data = await self.cache_manager.get_data(str(message.from_user.id))
        return bool(user_data) and self.has_cached_data in user_data




class StateFilter(BaseFilter):
    key = 'state_is'

    def __init__(self, state_is):
        self.state_is = state_is

    async def __call__(self, update: ChatMemberUpdated) -> bool:
        user_id = str(update.from_user.id)
        user_data = await self.cache_manager.get_data(user_id)
        return user_data.get("state") == str(self.state_is)