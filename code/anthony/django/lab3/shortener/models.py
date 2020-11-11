from django.db import models

# Model: a model ShortenedURL which has the following fields code(CharField), url(URLField)
# Add an IntegerField counter to the ShortenedUrl model,
# increment the counter every time the short url is accessed.
# Show the counter of each shortened url in the template.


class ShortenedURL(models.Model):
    code = models.CharField(max_length=7)
    url = models.URLField()
    count = models.IntegerField(default=0)

    # def __str__(self) behaves the same
    def __repr__(self):
        # (74BA194) - https://google.com/somethingsomethingsomething
        return f"({self.code}) - {self.url}"
