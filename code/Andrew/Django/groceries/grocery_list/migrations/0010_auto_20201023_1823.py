# Generated by Django 3.1.2 on 2020-10-24 01:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0009_auto_20201023_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery_item',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 24, 1, 23, 56, 740378, tzinfo=utc)),
        ),
    ]