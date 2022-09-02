from django.db import models

# Create your models here.

class ShortenedURL(models.Model):

    code = models.CharField(max_length=6)
    url = models.URLField(max_length=240)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.url


"""
Add an IntegerField counter to the ShortenedUrl model, 
increment the counter every time the short url is accessed. 
Show the counter of each shortened url in the template.


"""