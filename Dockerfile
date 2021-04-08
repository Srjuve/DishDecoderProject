FROM python:latest 
ENV DJANGO_SETTINGS_MODULE "DishDecoderProject.settings.production_docker"

RUN mkdir /app  

WORKDIR /app  

ADD requirements.txt /app/ 

RUN pip install -r requirements.txt 

ADD . /app/  

RUN python manage.py collectstatic --noinput
