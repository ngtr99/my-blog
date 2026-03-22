from django.db import models

# Create your models here.

class Post(models.Model):
    # models.py
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title