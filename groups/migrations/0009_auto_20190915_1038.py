# Generated by Django 2.1.5 on 2019-09-15 05:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_auto_20190915_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 10, 38, 43, 814028)),
        ),
    ]
