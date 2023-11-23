FROM williambutcherbot/python:latest

WORKDIR /app

# Copying Requirements and Installing Dependencies
COPY requirements.txt /app
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Copying Source Code
COPY . .

# Set appropriate permissions (adjust as needed)
RUN chmod 755 /app

# Starting Bot
CMD ["python3", "-m", "Key"]
