from django.db import models
from django.contrib.auth.models import User


# every class represents table in the database

class Person(models.Model):
    # fields of the table
    random_name = models.CharField(max_length=128)
    descriptor = models.CharField(max_length=200)

    # display names
    def __str__(self):
        return self.random_name

    def __unicode__(self):
        return self.random_name

    # display name of plural forms
    class Meta:
        verbose_name_plural = "persons"


class Camera(models.Model):
    name = models.CharField(max_length=20)
    product_number = models.CharField(max_length=128)
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Log(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField('Person seen at')

    def __str__(self):
        return str("Person:" + self.person.random_name + " seen at: " + self.camera.location)

    class Meta:
        verbose_name_plural = "logs"
