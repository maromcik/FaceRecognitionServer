# Face recognition server

You can use the provided script ```run.sh``` that accepts ```-b``` switch to build apps and migrate databases. Use this switch if running for the first time.

If you do not want to use the script you can build this app with standard Docker commands 
### Installation instructions
* Install ```docker``` and ```docker-compose```
* Clone this repository
* In current directory execute command ```docker-compose up --build```
* Then enter these commands: \
```docker-compose run app python3 manage.py migrate``` \
```docker-compose run app python3 manage.py createsuperuser```