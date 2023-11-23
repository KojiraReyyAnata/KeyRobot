FROM williambutcherbot/python:latest

WORKDIR /manage

# Copying Requirements and Installing Dependencies
COPY . .
RUN pip3 install --no-cache-dir -U -r requirements.txt

# If u want to use /update feature, uncomment the following and edit
#RUN git config --global user.email "your_email"
#RUN git config --global user.name "git_username"

# Copying Source Code
COPY . .

# Set appropriate permissions (adjust as needed)
RUN chmod 755 /manage

# Starting Bot
CMD ["python3", "-m", "Key"]
