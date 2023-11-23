FROM williambutcherbot/python:latest

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg neofetch \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY . /manage

WORKDIR /manage

RUN pip3 install -U pip \
    && pip3 install --no-cache-dir -U -r requirements.txt

CMD ["python3", "-m", "Key"]
