# Generated by Django 3.1.1 on 2020-10-22 02:08

from django.db import migrations, models
import todo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(default=5, validators=[todo.models.validate_range]),
        ),
    ]