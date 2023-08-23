# Получаем базовый образ
FROM python:3.8

# Уставнавиливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установите рабочую директорию
WORKDIR /dj_book_proj

# Уставнавиливаем зависимости
COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt
# Копирование проекта
COPY . /dj_book_proj/