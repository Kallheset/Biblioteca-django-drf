FROM python:3.11-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=biblioteca.settings
ENV DEBUG=False

# Instalar dependencias del sistema necesarias para mysqlclient
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        default-libmysqlclient-dev \
        pkg-config \
        python3-dev \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Crear directorio para archivos estáticos
RUN mkdir -p /app/staticfiles

# Exponer el puerto
EXPOSE 8000

# Script de inicio
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Comando para producción usando Gunicorn
CMD ["/start.sh"]
