# Generated by Django 3.1.2 on 2020-10-24 01:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0011_auto_20201023_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery_item',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grocery_item',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 24, 1, 27, 26, 532337, tzinfo=utc)),
        ),
    ]
