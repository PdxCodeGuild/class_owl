# Generated by Django 3.1.2 on 2020-10-29 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoot',
            name='created_date',
            field=models.DateTimeField(auto_created=True, default=1),
            preserve_default=False,
        ),
    ]
