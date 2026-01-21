FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY rag-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# код rag-приложения
COPY rag-app /app

# общий код
COPY common /app/common

ENV PYTHONPATH=/app

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8001"]
