# Generated by Django 4.1.2 on 2022-10-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0002_alter_unipi_camera1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id_in_dsc',
            field=models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='ID in the list of descriptors'),
        ),
    ]