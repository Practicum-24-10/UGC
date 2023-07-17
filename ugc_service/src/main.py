import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from ugc_service.src.api.v1 import views
from ugc_service.src.auth import rsa_key
from ugc_service.src.auth.abc_key import RsaKey
from ugc_service.src.core.config import PUBLIC_KEY, AppSettings
from ugc_service.src.core.logger import LOGGING
from ugc_service.src.db import kafka_db, redis_db
from ugc_service.src.db.cache import RedisCache
from ugc_service.src.db.storage import KafkaStorage

config = AppSettings()
app = FastAPI(
    title=config.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup():
    redis_db.redis = RedisCache(host=config.redis_host, port=config.redis_port)
    kafka_db.kf = KafkaStorage(
        host=config.kafka_host, port=config.kafka_port, topic=config.kafka_topic
    )
    rsa_key.pk = RsaKey(path=PUBLIC_KEY, algorithms=["RS256"])


@app.on_event("shutdown")
async def shutdown():
    if redis_db.redis:
        await redis_db.redis.close()
    if kafka_db.kf:
        await kafka_db.kf.stop()


app.include_router(views.router, prefix="/api/v1/views", tags=["views"])

if __name__ == "__main__":
    logging.basicConfig(**LOGGING)
    log = logging.getLogger(__name__)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
