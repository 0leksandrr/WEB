# Використовуємо базовий образ Python версії 3.12.1
FROM python:3.11.7

# Оновлюємо pip
RUN pip install --upgrade pip

# Встановлюємо змінні середовища для уникнення створення байткоду та безбуферного виводу Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Створюємо нову директорію для віртуального середовища
RUN mkdir /venv

# Створюємо та активуємо віртуальне середовище
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Копіюємо файли проекту в контейнер
COPY . /WEB

# Встановлюємо залежності за допомогою pip
WORKDIR /WEB
RUN pip install --no-cache-dir -r requirements.txt

# Запускаємо Gunicorn для обробки веб-запитів
CMD ["python", "/WEB/kursova/manage.py", "runserver", "127.0.0.1:8000"]




