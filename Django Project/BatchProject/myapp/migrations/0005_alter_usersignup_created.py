# Generated by Django 4.0 on 2022-11-07 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_usersignup_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2022, 11, 7, 16, 40, 7, 887790)),
        ),
    ]
