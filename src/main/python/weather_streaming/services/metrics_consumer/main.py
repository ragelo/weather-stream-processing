from kafka import KafkaConsumer
from time import sleep
from weather_streaming.config import KAFKA_URL, WEATHER_METRICS_TOPIC

consumer = KafkaConsumer(
    bootstrap_servers=KAFKA_URL,
    client_id="weather-consumer",
    api_version=(2, 4, 0),
)

consumer.subscribe(WEATHER_METRICS_TOPIC)

while True:
    partitions = consumer.poll(timeout_ms=1000, max_records=100)
    for partition in partitions:
        for message in partitions[partition]:
            print(message.value.decode("utf-8"))
        
    
    if len(partitions) == 0:
        print("No messages")
        sleep(1)
