# Generated by Django 4.1.2 on 2022-10-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0002_alter_room_visited'),
    ]

    operations = [
        migrations.AddField(
            model_name='unipi',
            name='server_ip',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
    ]