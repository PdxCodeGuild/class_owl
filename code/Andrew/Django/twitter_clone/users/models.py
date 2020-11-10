from django.db import models

# Create your models here.

class CreateUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=23)
    date_created = models.DateTimeField()

   