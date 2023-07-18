from pydantic import BaseSettings


class TestSettings(BaseSettings):
    redis: str = "redis"
    redis_port: int = 6379
    service_url: str = "http://localhost/api/v1/"


test_settings = TestSettings()
