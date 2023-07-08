from kafka import KafkaProducer

kf: KafkaProducer | None = None


async def get_kafka() -> KafkaProducer | None:
    return kf
