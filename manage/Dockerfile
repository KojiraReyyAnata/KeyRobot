FROM williambutcherbot/python:latest

WORKDIR /app

COPY . /app


RUN pip3 install -U pip

RUN pip3 install --no-cache-dir -U -r requirements.txt


CMD ["python3", "-m", "Key"]
