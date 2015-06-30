from django.db import models


class Rater(models.Model):
    user_id = models.IntegerField(primary_key=True)


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)


# Create your models here.
class Link(models.Model):
    movie = models.ForeignKey(Movie)
    imdb = models.CharField(max_length=7)
    tmdb = models.IntegerField()

    def __str__(self):
        return str(self.movie)


class Tag(models.Model):
    user = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    tag = models.CharField(max_length=150)
    timestamp = models.IntegerField()


class Rating(models.Model):
    user = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()
