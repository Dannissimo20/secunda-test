FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY src/ ./src/
COPY alembic.ini .
COPY alembic/ ./alembic/

# Команда по умолчанию (может быть переопределена в docker-compose)
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]