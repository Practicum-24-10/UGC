from abc import ABC, abstractmethod

from kafka import KafkaProducer


class AbstractStorage(ABC):
    @abstractmethod
    def send(self, key: str, value: str):
        pass

    @abstractmethod
    def close(self):
        pass


class KafkaStorage(AbstractStorage):
    def __init__(self, host: str, port: str, topic: str):
        self._connect = KafkaProducer(bootstrap_servers=[f'{host}:{port}'])
        self.topic = topic

    def send(self, key: str, value: str):
        return self._connect.send(
            topic=self.topic,
            value=bytes(value, "utf-8"),
            key=bytes(key, "utf-8"),)

    def close(self):
        self._connect.close()
