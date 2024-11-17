FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /web

COPY requirements.txt /web/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /web/

ARG DJANGO_PORT
ENV DJANGO_PORT=${DJANGO_PORT}

EXPOSE ${DJANGO_PORT}

RUN python manage.py makemigrations --noinput
