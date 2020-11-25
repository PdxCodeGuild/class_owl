from django.db import models

# Create your models here.
class Glist(models.Model):
    item = models.CharField(max_length=200),
    brand = models.CharField(max_length=200),

def __str__(self):
    return self.title + ' - ' + self.author