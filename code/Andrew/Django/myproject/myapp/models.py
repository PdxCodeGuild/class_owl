from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    date_published = models.DateTimeField()
    likes = models.IntegerField()



    def __str__(self):
        return self.title + ' - ' + self.author