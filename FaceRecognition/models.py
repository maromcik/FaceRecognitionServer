import os

from cryptography.fernet import Fernet
from django.db import models
from API import FaceRecAPI
from FaceRecognitionServer import settings


class PasswordField(models.CharField):
    description = "Encrypted password"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 1024
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def get_prep_value(self, value):
        f = Fernet(settings.PASSWORD_KEY)
        print("getprepval", value)
        if value is None:
            return ""
        encrypted = f.encrypt(value.encode('utf-8'))
        return encrypted.decode('utf-8')

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        f = Fernet(settings.PASSWORD_KEY)
        decrypted = f.decrypt(value.encode('utf-8'))
        return decrypted.decode('utf-8')

    def to_python(self, value):
        if isinstance(value, SSHProfile):
            return value
        if value is None:
            return value
        # f = Fernet(settings.PASSWORD_KEY)
        # print("PYTHON", value)
        # decrypted = f.decrypt(value.encode('utf-8'))
        # return decrypted.decode('utf-8')
        return value



class Person(models.Model):
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "persons"


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to="")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "staff"


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    visited = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class SSHProfile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    encrypted_password = PasswordField(max_length=1024)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name_plural = "SSHProfiles"


class Server(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=255, default=os.environ.get("SERVER_IP", default=FaceRecAPI.infer_ip()))

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Servers"


class Camera(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    stream = models.CharField(max_length=255)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    entrance = models.BooleanField(default=False)
    exit = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    cameras = models.ManyToManyField(Camera)
    server = models.ForeignKey(Server, on_delete=models.PROTECT)
    ssh_profile = models.ForeignKey(SSHProfile, on_delete=models.PROTECT)
    ssh_access = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Clients"


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField('Seen at')

    def __str__(self):
        return "Person " + str(self.person.id) + " seen at " + self.camera.room.name

    def __unicode__(self):
        return "Person " + str(self.person.id) + " seen at " + self.camera.room.name

    class Meta:
        verbose_name_plural = "logs"


# class ClientCamera(models.Model):
#     id = models.AutoField(primary_key=True)
#



