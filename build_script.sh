#!/bin/bash
python manage.py migrate

#python manage.py runserver 0.0.0.0:8000
gunicorn -b 0.0.0.0:8000 DishDecoderProject.wsgi:application --timeout 200 --workers 3
