from django.db import models

# Create your models here.


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    length = models.PositiveIntegerField(help_text="Length of song in seconds")
    release_date = models.DateField(auto_now=True)
    genre = models.CharField(max_length=100)
