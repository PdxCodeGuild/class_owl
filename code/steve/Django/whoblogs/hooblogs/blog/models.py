from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hoot(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    image = models.CharField(max_length=512, null=True, blank=True)
    total_likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

# Each class must have the str module and have a return
    def __str__(self):
        return self.title

    

# CASCADE deletes all the records associated to Hoot Class

class Comment(models.Model):
    hoot = models.ForeignKey(Hoot, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    
    
    def __str__(self):
        return self.body


