# Generated by Django 2.1.5 on 2019-09-15 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20190915_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fac',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 10, 59, 7, 329723)),
        ),
    ]
