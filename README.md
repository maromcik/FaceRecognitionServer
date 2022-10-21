# Face recognition server


### Installation instructions
* Install ```docker``` and ```docker-compose```
* Clone this repository
* In current directory execute command ```docker-compose up --build```
* Then enter these commands: \
```docker-compose run app python3 manage.py migrate``` \
```docker-compose run app python3 manage.py createsuperuser```