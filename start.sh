#!/bin/bash

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Iniciar Gunicorn
exec gunicorn biblioteca.wsgi:application --bind 0.0.0.0:8000 --workers 3 