# Face Recognition Server
This application allows tracking customers around premises of a company. 

It receives detected and aligned faces from client devices (see [FaceRecognition](https://github.com/maromcik/FaceRecognition)) and performs face recognition on them and logs their movement. Faces of staff are ignored.
The management interface is build using Django.
The clients are configured via this server.

### Installation instructions
* Install [Docker](https://docs.docker.com/engine/install/ubuntu/) and [Docker Compose](https://docs.docker.com/compose/install/linux/#install-using-the-repository)
* Clone this repository
* In current directory execute command ```docker-compose up --build```
* Then enter these commands: \
```docker-compose run app python3 manage.py migrate``` \
```docker-compose run app python3 manage.py createsuperuser```

You can use the provided script ```run.sh``` to run the application (executes ```docker-compose up```).

Furthermore, it accepts the following switches:
* ```-b``` - to build the images and execute ```docker-compose run app python3 manage.py migrate``` to migrate the database.
* ```-s``` - to create a superuser by executing ```docker-compose run app python3 manage.py createsuperuser```
 
