import logging
from functools import lru_cache
from uuid import UUID

from ugc_service.src.db.cache import AbstractCache
from ugc_service.src.db.kafka_db import get_kafka
from ugc_service.src.db.redis_db import get_redis
from ugc_service.src.db.storage import AbstractStorage
from fastapi import Depends

from ugc_service.src.services.mixin import MixinModel

log = logging.getLogger(__name__)


class ViewsService(MixinModel):
    async def add_new_data(self, user_id: UUID, film_id: UUID, timestamp: int):
        mixin_id = f"{user_id}:{film_id}"
        try:
            await self._put_to_storage(mixin_id, user_id, film_id, str(timestamp))
            await self._put_to_cache(mixin_id, str(timestamp))
            return True
        except Exception as er:
            log.error(er)
            return False

    async def get_film_time(self, user_id: UUID, film_id: UUID):
        mixin_id = f"{user_id}:{film_id}"
        return await self._get_from_cache(mixin_id)


@lru_cache()
def get_views_service(
        redis: AbstractCache = Depends(get_redis),
        kafka: AbstractStorage = Depends(get_kafka),
) -> ViewsService:
    return ViewsService(redis, kafka)
