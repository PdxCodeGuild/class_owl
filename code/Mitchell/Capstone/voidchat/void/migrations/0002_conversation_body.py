# Generated by Django 3.1.2 on 2020-11-24 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('void', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='body',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
    ]
