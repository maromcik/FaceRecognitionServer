import os

from django.db import models
from API import FaceRecAPI


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
    name = models.CharField(max_length=50)
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
    username = models.CharField(max_length=255, default="pi")
    password = models.CharField(max_length=255, default="raspberry")
    server_ip = models.CharField(max_length=255, default=os.environ.get("SERVER_IP", default=FaceRecAPI.infer_ip()))
    camera1 = models.ForeignKey(Camera, on_delete=models.CASCADE, related_name="camera1")
    camera2 = models.ForeignKey(Camera, on_delete=models.CASCADE, related_name="camera2", default=None, null=True, blank=True)
    ssh = models.BooleanField(default=True)

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
