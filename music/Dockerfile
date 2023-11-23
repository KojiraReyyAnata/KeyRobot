FROM python:3.10

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg neofetch \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /app

COPY manage .


RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

# Starting Bot
CMD bash start