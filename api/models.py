from django.db import models

# Create your models here.
from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    length = models.PositiveIntegerField(help_text="Length of song in seconds")
    release_date = models.DateField(auto_now=True, auto_now_add=True)
    genre = models.CharField(max_length=100)
