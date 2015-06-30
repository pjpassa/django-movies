from django.db import models

# Create your models here.
class Links(models.Model):
    movieId = models.IntegerField(primary_key=True)
    imdbId = models.CharField(max_length=7)
    tmdbId = models.IntegerField()
