from aioredis import Redis

redis: Redis | None = None


async def get_redis() -> Redis | None:
    return redis
