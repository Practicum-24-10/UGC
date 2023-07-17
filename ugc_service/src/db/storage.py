import json
from abc import ABC, abstractmethod

from aiokafka import AIOKafkaProducer


class AbstractStorage(ABC):
    @abstractmethod
    async def send(self, key: str, user_id, film_id, value: str):
        pass


class KafkaStorage(AbstractStorage):
    def __init__(self, host: str, port: str, topic: str):
        self._producer = AIOKafkaProducer(
            bootstrap_servers=f"{host}:{port}",
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        self.topic = topic

    async def send(self, key: str, user_id, film_id, value: str):
        await self._producer.start()
        return await self._producer.send_and_wait(
            topic=self.topic,
            value={
                "user_id": str(user_id),
                "film_id": str(film_id),
                "film_timestamp": value,
            },
            key=bytes(key, "utf-8"),
        )
