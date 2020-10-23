from django.db import models

# Create your models here.
class groceryItem(models.Model):
    item = models.CharField(max_length=200)
    created = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    amount = models.IntegerField(default=0)
def __str__(self):
    return self.item    