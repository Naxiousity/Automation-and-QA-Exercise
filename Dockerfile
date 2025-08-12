FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (optional, like curl)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (so it's cached unless requirements.txt changes)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the code after installing dependencies
COPY . .

# Run tests by default (or override via docker-compose or command line)
CMD ["pytest", "tests/test_login.py"]
