import json
from abc import ABC, abstractmethod

from kafka import KafkaProducer


class AbstractStorage(ABC):
    @abstractmethod
    def send(self, key: str, user_id, film_id, value: str):
        pass

    @abstractmethod
    def close(self):
        pass


class KafkaStorage(AbstractStorage):
    def __init__(self, host: str, port: str, topic: str):
        self._connect = KafkaProducer(
            bootstrap_servers=[f"{host}:{port}"],
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        self.topic = topic

    def send(self, key: str, user_id, film_id, value: str):
        return self._connect.send(
            topic=self.topic,
            value={
                "user_id": str(user_id),
                "film_id": str(film_id),
                "film_timestamp": value,
            },
            key=bytes(key, "utf-8"),
        )

    def close(self):
        self._connect.close()
