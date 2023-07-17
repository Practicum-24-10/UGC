from abc import ABC, abstractmethod

from redis import asyncio as aioredis


class AbstractCache(ABC):
    @abstractmethod
    async def get(self, _id: str):
        pass

    @abstractmethod
    async def set(self, _id: str, data: str):
        pass

    @abstractmethod
    async def close(self):
        pass


class RedisCache(AbstractCache):
    def __init__(self, host: str, port: int):
        self._connect = aioredis.Redis(host=host, port=port)

    async def get(self, _id: str):
        return await self._connect.get(name=_id)

    async def set(self, _id: str, data: str):
        return await self._connect.set(name=_id, value=data)

    async def close(self):
        await self._connect.close()
