# Generated by Django 4.1.2 on 2022-11-01 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0009_alter_unipi_server_ip'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Unipi',
            new_name='Client',
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name_plural': 'Clients'},
        ),
    ]