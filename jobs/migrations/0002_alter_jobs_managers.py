# Generated by Django 3.2.9 on 2021-11-24 05:39

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='jobs',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
