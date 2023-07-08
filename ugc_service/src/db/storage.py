from abc import ABC, abstractmethod

from kafka import KafkaProducer


class AbstractStorage(ABC):
    @abstractmethod
    def send(self, data: dict):
        pass

    @abstractmethod
    def close(self):
        pass


class KafkaStorage(AbstractStorage):
    def __init__(self, hosts: list[str]):
        self._connect = KafkaProducer(bootstrap_servers=hosts)

    def send(self, data: dict):
        return self._connect.send(**data)

    def close(self):
        self._connect.close()
