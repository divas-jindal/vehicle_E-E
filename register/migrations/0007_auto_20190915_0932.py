# Generated by Django 2.1.5 on 2019-09-15 04:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20190915_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fac',
            name='time_in',
        ),
        migrations.AddField(
            model_name='fac',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 9, 32, 31, 851033)),
        ),
    ]
