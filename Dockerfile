FROM python:3.11.4-slim-buster

ENV PYTHONDONTWRITEBYTECODE='1'
ENV PYTHONUNBUFFERED='1'

WORKDIR /app/

RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  libpq-dev \
  git


COPY ./.env /app/

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./core /app/