from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    id_in_dsc = models.CharField(max_length=10, verbose_name="ID in the list of descriptors")
    def __str__(self):
        return self.id_in_dsc

    def __unicode__(self):
        return self.id_in_dsc

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


class Unipi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    username = models.CharField(max_length=255, default="pi")
    password = models.CharField(max_length=255, default="raspberry")
    server_ip = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Unipis"


class Camera(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    stream = models.CharField(max_length=255)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    unipi = models.ForeignKey(Unipi, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Log(models
          .Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField('Seen at')

    def __str__(self):
        return str("Person " + self.person.id_in_dsc + " seen at " + self.camera.room.name)

    def __unicode__(self):
        return str("Person " + self.person.id_in_dsc + " seen at " + self.camera.room.name)

    class Meta:
        verbose_name_plural = "logs"


