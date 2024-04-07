FROM python:3.12-slim
RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY src/main/python/weather_streaming ./weather_streaming
ENV PYTHONPATH=/app

CMD ["python", "weather_streaming/services/metrics_producer/main.py"]
