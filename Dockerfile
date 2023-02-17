FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

ENV HOUSECANARY_API_KEY=fakehousecanarykey1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/