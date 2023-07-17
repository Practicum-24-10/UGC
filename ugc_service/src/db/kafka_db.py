from aiokafka import AIOKafkaProducer

kf: AIOKafkaProducer | None = None


async def get_kafka() -> AIOKafkaProducer | None:
    return kf
