#!/bin/bash
build=false

while getopts ":b" option; do
  case $option in
    h) echo "usage: $0 [-h] [-b]"; exit ;;
    b) build=true ;;
    ?) echo "error: option -$OPTARG does not exist - specify -b if you want to build for the first time"; exit ;;
  esac
done
shift $(( OPTIND - 1 ))

if [ "$build" = true ] ; then
  sudo docker-compose build
	docker-compose run app python3 manage.py migrate
  docker-compose run app python3 manage.py createsuperuser
fi

docker-compose up
