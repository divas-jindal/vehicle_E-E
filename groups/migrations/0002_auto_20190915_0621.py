# Generated by Django 2.1.5 on 2019-09-15 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='guest',
            name='vehicle_no',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
