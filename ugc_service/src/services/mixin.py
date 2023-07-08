from abc import ABC, abstractmethod

from ugc_service.src.db.cache import AbstractCache
from ugc_service.src.db.storage import AbstractStorage


class AbstractMixin(ABC):
    @abstractmethod
    async def _put_to_cache(self, method: str, data: str | dict):
        pass

    @abstractmethod
    async def _get_from_cache(self, _id: bytes) -> bytes | None:
        pass

    @abstractmethod
    async def _put_to_storage(self, _id: str, data: str):
        pass


class MixinModel(AbstractMixin):
    def __init__(self, cache: AbstractCache, storage: AbstractStorage):
        self.cache = cache
        self.storage = storage

    async def _get_from_cache(self, _id: str) -> bytes | None:
        """
        Получения данных по id
        :param _id: id для доступа
        :return: данные
        """
        data = await self.cache.get(_id)
        if not data:
            return None
        return data

    async def _put_to_cache(self, _id: str, data: str):
        """
        Сохраняет в кеш данные
        :param _id: id для доступа
        :param data: данные
        """
        await self.cache.set(_id, data)

    async def _put_to_storage(self, _id: str, data: str):
        """
        Сохраняет в хранилища данные
        :param _id: id для доступа
        :param data: данные
        """
        pass
