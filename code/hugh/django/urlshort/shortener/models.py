from django.db import models
from django.db.models.fields import CharField

# Create your models here.
#ShortenedURL with fields(CharField) and (URLField)
class ShortenedURL(models.Model):
    code = models.CharField(max_length=7)
    url = models.URLField()
    count = models.IntegerField(default=0)
    
    def __string__(self):
        return f"({self.code} - {self.url})"