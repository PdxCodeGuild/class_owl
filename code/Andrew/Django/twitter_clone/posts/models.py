from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.


class Chirp(models.Model):

    user = models.ForeignKey(User, on_delete= CASCADE)
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    likes = models.IntegerField(default = 0)


    def __str__(self):
        return self.message


    
