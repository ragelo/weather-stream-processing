from time import sleep
from kafka import KafkaProducer

from weather_streaming.config import KAFKA_URL, WEATHER_METRICS_TOPIC

producer = KafkaProducer(bootstrap_servers=KAFKA_URL)

while True:
    for _ in range(100):
        producer.send(WEATHER_METRICS_TOPIC, b"Hello, World!")
    producer.flush()

    sleep(.01)
