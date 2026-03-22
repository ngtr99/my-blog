from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.title