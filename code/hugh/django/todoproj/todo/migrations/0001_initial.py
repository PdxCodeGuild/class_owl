# Generated by Django 3.2.dev20201020074905 on 2020-10-22 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('priority', models.IntegerField(default=0)),
                ('date_completed', models.DateField(blank=True, null=True)),
            ],
        ),
    ]