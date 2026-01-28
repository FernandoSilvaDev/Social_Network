FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip && pip install -r /app/requirements.txt

# Dependências mínimas necessárias
RUN apt-get update && \
    apt-get install -y gcc libpq-dev --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install poetry

# Copia apenas pyproject/lock para cache
COPY pyproject.toml poetry.lock* /app/

# Ativa virtualenv dentro do container (mais leve no Render)
RUN poetry config virtualenvs.create true \
    && poetry install --no-root --no-interaction --no-ansi

COPY . /app

#ENV DJANGO_SETTINGS_MODULE=social_network.settings

# Static files
RUN poetry run python manage.py collectstatic --noinput

EXPOSE 8000
ENV PYTHONUNBUFFERED=1
# CMD ["gunicorn", "social_network.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD poetry run gunicorn social_network.wsgi:application --bind 0.0.0.0:$PORT
