from django.db import models
from django.utils import timezone
# Create your models here.


class Grocery_item( models.Model):
   
    description=  models.CharField(max_length=200)
    created_date= models.DateField(default =timezone.now())
    completed_date= models.DateField (null= True, blank=True)
    completed= models.BooleanField(default= False)


    def __str__(self):
        return self.description