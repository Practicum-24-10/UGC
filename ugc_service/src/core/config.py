import os
from logging import config as logging_config

import dotenv
from pydantic import BaseSettings

from ugc_service.src.core.logger import LOGGING

logging_config.dictConfig(LOGGING)
dotenv.load_dotenv()


class AppSettings(BaseSettings):
    project_name: str = "Some project name"
    redis_host: str = "localhost"
    redis_port: int = 6379
    kafka_host: str = "localhost"
    kafka_port: str = "9092"
    kafka_topic: str = 'some_topic'


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PUBLIC_KEY_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PUBLIC_KEY = os.path.join(PUBLIC_KEY_DIR, os.environ.get("PUBLIC_KEY"))
