# Generated by Django 4.1.2 on 2022-11-12 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0012_alter_client_server_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('ip', models.CharField(default='192.168.1.52', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='SSHProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='pi', max_length=255)),
                ('password', models.CharField(default='raspberry', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'SSHProfiles',
            },
        ),
        migrations.RenameField(
            model_name='client',
            old_name='ssh',
            new_name='ssh_access',
        ),
        migrations.RemoveField(
            model_name='client',
            name='password',
        ),
        migrations.RemoveField(
            model_name='client',
            name='server_ip',
        ),
        migrations.RemoveField(
            model_name='client',
            name='username',
        ),
        migrations.AddField(
            model_name='client',
            name='server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FaceRecognition.server'),
        ),
        migrations.AddField(
            model_name='client',
            name='ssh_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FaceRecognition.sshprofile'),
        ),
    ]
