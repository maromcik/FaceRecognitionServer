FROM ubuntu:latest
WORKDIR /FaceRecognitionServer

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Bratislava


RUN apt-get update && apt-get upgrade -y
RUN apt-get install apt-utils cmake git python3-pip python3-dev libpq-dev postgresql postgresql-contrib build-essential ffmpeg libsm6 libxext6 musl-dev libc-dev -y
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN ls