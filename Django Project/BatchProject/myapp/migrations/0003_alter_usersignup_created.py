# Generated by Django 4.0 on 2022-11-07 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_usersignup_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 11, 7, 16, 37, 39, 410857)),
        ),
    ]