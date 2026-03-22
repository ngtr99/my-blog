from django.db import models

# Create your models here.

class Post(models.Model):
    # models.py
    image = models.URLField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title