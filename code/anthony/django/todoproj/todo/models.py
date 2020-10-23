from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

# Create your models here.


def validate_range(value):
    if value < 0 or value > 10:
        raise ValidationError(
            gettext_lazy(f'{value} is not with the range of 0 - 10'),
            params={'value': value},
        )


class Todo(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=5, validators=[validate_range])
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task
