from django.db import models


# Create your models here.
class Rater(models.Model):
    rater = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=200)


class Link(models.Model):
    movie = models.ForeignKey(Movie)
    imdb = models.CharField(max_length=7)
    tmdb = models.CharField(max_length=7)

    def __str__(self):
        return str(self.movie)


class Tag(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    tag = models.CharField(max_length=150)
    timestamp = models.IntegerField()


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()


class Movie_Genre(models.Model):
    movie = models.ForeignKey(Movie)
    genre = models.CharField(max_length=100)