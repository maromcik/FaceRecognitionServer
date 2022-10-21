FROM python:3.10.5-alpine
WORKDIR /root/FaceRecognitionServer

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apk update && apk upgrade
RUN apk add cmake git python3-dev mariadb-dev g++ gcc
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .