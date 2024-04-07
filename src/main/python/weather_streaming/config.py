import os
WEATHER_METRICS_TOPIC = "weatherstation-events"

KAFKA_URL = os.environ.get("KAFKA_BROKERS", "localhost:9092")
