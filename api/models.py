from django.db import models
import datetime

# Create your models here.


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    length = models.PositiveIntegerField(help_text="Length of song in seconds")
    release_date = models.DateField(default=datetime.date.today)
    genre = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)
