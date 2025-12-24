FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=1000 --retries 10 -r requirements.txt


COPY . .

CMD ["python", "build_index.py"]
