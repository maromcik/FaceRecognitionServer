from django.db import models
from django.contrib.auth.models import User


# every class represents table in the database

class Person(models.Model):
    # fields of the table
    id = models.AutoField(primary_key=True)
    id_in_dsc = models.CharField(max_length=10)

    # display names
    def __str__(self):
        return self.id_in_dsc

    def __unicode__(self):
        return self.id_in_dsc

    # display name of plural forms
    class Meta:
        verbose_name_plural = "persons"


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    file = models.ImageField(upload_to="")

    # display names
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    # display name of plural forms
    class Meta:
        verbose_name_plural = "staff"


class Camera(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    product_number = models.CharField(max_length=128)
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField('Person seen at')

    def __str__(self):
        return str("Person:" + self.person.id_in_dsc + " seen at: " + self.camera.location)

    class Meta:
        verbose_name_plural = "logs"
