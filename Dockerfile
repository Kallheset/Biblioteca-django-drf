FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalar dependencias del sistema necesarias para mysqlclient, pillow, etc.
RUN apt-get update && apt-get install -y \
    build-essential \
    libmysqlclient-dev \
    default-libmysqlclient-dev \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

# Dar permisos de ejecución al script de inicio
RUN chmod +x /app/start.sh

EXPOSE 8000
CMD ["sh", "/app/start.sh"]