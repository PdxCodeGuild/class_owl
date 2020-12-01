from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as gettext_lazy

# Create your models here.
def validate_range(value):
        if value < 1 or value > 10:
            raise ValidationError(
                gettext_lazy(f'{value} is not within the range of 1-10'),
                params={'value': value},
            )


class GroceryList(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateField(null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.task

    