FROM python:3.11-slim

WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY project/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Code comes from bind mount in docker-compose
# COPY project/ .   <-- intentionally removed because we have linked

EXPOSE 5000

CMD ["python", "app.py"]

