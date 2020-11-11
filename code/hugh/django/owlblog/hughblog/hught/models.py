from django.db import models
from django.urls.base import translate_url
from django.utils import timezone
from django.utils.timezone import localdate

# Create your models here.
class Hught(models.Model):
    title = models.CharField(max_length=24)
    body = models.CharField(max_length=70)
    # Author
    publishdate = models.DateTimeField(blank = True, null=True)
    ispublished = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    image = models.CharField(max_length=512,null=True,blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    hught = models.ForeignKey(Hught, on_delete=models.CASCADE)
    body = models.CharField(max_length=70)
    # Author
    posteddate = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.body