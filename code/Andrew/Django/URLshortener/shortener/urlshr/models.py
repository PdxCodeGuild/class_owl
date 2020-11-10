from django.db import models

# Create your models here.


class ShortenedURL(models.Model):

    url = models.URLField(max_length=250)
    code = models.CharField(max_length=250)
    visited = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.code} : ({self.url})' 
        
