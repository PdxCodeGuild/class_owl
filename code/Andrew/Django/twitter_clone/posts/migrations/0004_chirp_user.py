# Generated by Django 3.1.2 on 2020-11-07 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('posts', '0003_remove_chirp_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chirp',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.createuser'),
            preserve_default=False,
        ),
    ]