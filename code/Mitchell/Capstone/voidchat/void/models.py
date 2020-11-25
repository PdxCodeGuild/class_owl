from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Conversation(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=False)
    likes =models.IntegerField(default=0)
    image = models.CharField(max_length=512, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    body =models.CharField(max_length=25)
    voicefile =models.FileField(upload_to="voicefiles")
    

    def __str(self):
        return self.title

class Comment(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    body =models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    file =models.FileField()

    def __str__(self):
        return self.body

class MyModel(models.Model):
    my_image = models.FileField(upload_to='images/')