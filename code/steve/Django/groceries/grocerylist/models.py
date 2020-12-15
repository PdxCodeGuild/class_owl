from django.db import models

# Create your models here.

class GroceryList(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description