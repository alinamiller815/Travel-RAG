# Использование минимального  имейджа уменьшает размер образа, ускоряет скачивание и снижает поверхность атаки
FROM python:3.10-slim

# Установка только необходимых системных зависимостей (--no-install-recommends) 
# и исключает лишние пакеты и делает образ легче
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Создание non-root пользователя
RUN useradd -m appuser

# рабочая директория
WORKDIR /app

# Копирование requirements.txt перед копированием всего проекта
# позволяет Docker использовать кэш слоёв и не переустанавливать зависимости при изменении кода
COPY COPY requirements.txt

# устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем только код
COPY src ./src

# Объявляем volume для данных RAG (индекс, чанки текстов, эмбеддинги и мета данные)
VOLUME ["/app/data"]

# Запуск приложения от non-root пользователя повышает безопасность 
# контейнера и снижает риски при уязвимостях в приложении
USER appuser

# Использование ENTRYPOINT для основного процесса
# гарантирует, что контейнер всегда запускает нужное приложение
ENTRYPOINT ["python", "-m", "src.main"]
CMD []