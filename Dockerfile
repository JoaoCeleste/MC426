FROM python:3.11.5-slim

WORKDIR /MC426

COPY requirements.txt requirements.txt 
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip3 install -r requirements.txt

COPY . .