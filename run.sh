#!/bin/bash
build=false
superuser=false

while getopts ":bs" option; do
  case $option in
    h) echo "usage: $0 [-h] [-b] [-s]"; exit ;;
    b) build=true ;;
    s) superuser=true ;;
    ?) echo "error: option -$OPTARG does not exist - specify -b if you want to build for the first time or -s if you want to create a superuser"; exit ;;
  esac
done
shift $(( OPTIND - 1 ))

if [ "$build" = true ] ; then
  sudo docker-compose build
	docker-compose run app python3 manage.py migrate
fi

if [ "$superuser" = true ] ; then
  docker-compose run app python3 manage.py createsuperuser
fi

docker-compose up
