FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app


RUN apt-get update && \
    apt-get install -y gcc libpq-dev --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/


RUN poetry config virtualenvs.create true \
    && poetry install --no-root --no-interaction --no-ansi

COPY . /app

ENV DJANGO_SETTINGS_MODULE=core.settings


RUN poetry run python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["bash", "-c", "poetry run python manage.py migrate --noinput && poetry run gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 1 --threads 2 --timeout 120"]