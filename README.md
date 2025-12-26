# AI Guide — Setup

## Локальный запуск


## 🚀 1. Установка окружения 
Создайте conda-окружение:

```bash
conda env create -f environment.yml
conda activate ai-guide
```

## 🔑 2. Настройка ключей

Создайте файл .env в корне проекта по образцу .env.example:

```
MISTRAL_API_KEY=your_api_key_here
```

## 🔑 📥 3. Скачать данные

1. Скачайте архив data/ с Google Drive:
<https://drive.google.com/file/d/1o9sy59wAFY2utvUHcCxLMOJaSIxFqkQd/view?usp=sharing>

2. Распакуйте в корень проекта:

```text
AI-guide/
  data/
    passages.json
    embeddings.faiss
    vector_store.pkl
    ...
```

## ▶️ 4. Запуск RAG-пайплайна

- python main.py --q "France visa?"

- либо poetry run python main.py --q "France visa?"

Вопрос можно/нужно менять!!!

---

## Запуск из контейнера

###  1. Сборка образа 

```
docker build -t rag .
```


###  2. Запуск контейнера 

```
docker build -f Dockerfile -t app .
docker run -d -v $(pwd)/data:/app/data app

```
###  3. Запуск сервиса 
```
python main.py --q "France visa?" 
```


## Отчет по lab1

В репозитории два докер файла: хороший Dockerfile, и плохой Dockerfile_bad.

### Bad practicies список:
 1.  Выбрана не самая легкая версия питона - 3.10 (в хорошем файле - 3.10 slim, облегченная). Использование минимального base уменьшает размер образа, ускоряет скачивание и снижает поверхность атаки

 2. Копируем проект раньше установки зависимостей - при изменениях в коде придется пересобирать весь образ заново

 3. Можно было бы положить в контейнер данные с индексами (папка data) - как вариант bad practice, но я сделала так, что можно скачать данные по ссылке или собрать нужные данные скриптом (buil_index.py)

 4. Использование CMD вместо ENTRYPOINT

 5. Запуск приложения от root - потенциальная угроза безопасности


### Когда не стоит использовать контейнеры вообще:
- Приложения с жёсткой привязкой к железу
- Системы реального времени, в которых важна минимальная задержка