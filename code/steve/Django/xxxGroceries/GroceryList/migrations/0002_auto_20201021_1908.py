# Generated by Django 3.1.2 on 2020-10-22 02:08

from django.db import migrations, models
import GroceryList.models


class Migration(migrations.Migration):

    dependencies = [
        ('Groceries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='GroceryList',
            name='priority',
            field=models.IntegerField(default=5, validators=[GroceryList.models.validate_range]),
        ),
    ]
