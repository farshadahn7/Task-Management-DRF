FROM python:3.11.4-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

ENV PYTHONDONTWRITEBYTECODE='1'
ENV PYTHONUNBUFFERED='1'

WORKDIR /app/
RUN pip install --upgrade pip
COPY ./.env /app/
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./core /app/
