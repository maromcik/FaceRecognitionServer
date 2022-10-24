#!/bin/bash
sudo docker-compose build
docker-compose run app python3 manage.py migrate
docker-compose run app python3 manage.py createsuperuser
docker-compose up