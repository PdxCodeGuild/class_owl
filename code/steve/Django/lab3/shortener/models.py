from django.db import models

# Model: a model ShortenedURL which has the following fields code (CharField), 
# url (URLField)
# Add an IntegerField counter to the ShortenedUrl model,
# Increment the counter every time the short URL is accessed
# Show the counter of each shortened URL in the template

class ShortenedURL(models.Model):
        code = models.CharField(max_length=7)
        url = models.URLField()
        count = models.IntegerField(default=0)

        # def __str_(self) behaves the same
        def __repr__(self):
            #(74BA194) - https://google.com/somethingsomethingsomethib
            return f"({self.code}) - {self.url}"