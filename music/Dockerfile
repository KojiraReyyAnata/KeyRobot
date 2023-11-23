FROM python:3.10

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY music /app

WORKDIR /app

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

CMD bash start
