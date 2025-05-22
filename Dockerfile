FROM python:3.9-slim

# Environment config
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Default command to run tests
CMD ["pytest", "tests"]
