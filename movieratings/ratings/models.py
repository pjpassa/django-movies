from statistics import mean
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Rater(models.Model):
    user = models.OneToOneField(User)
    rater = models.IntegerField()

    def __str__(self):
        return str(self.rater)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    average_rating = models.FloatField()

    def __str__(self):
        return self.title

    def calculate_average_rating(self):
        ratings = [rating.rating for rating in Rating.objects.filter(movie=self)]
        if ratings:
            self.average_rating = mean(ratings)
            self.save()


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

    def __str__(self):
        return " - ".join([str(self.movie), self.tag])


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.FloatField()
    timestamp = models.IntegerField()

    def __str__(self):
        return " - ".join([str(self.movie), str(self.rating)])


class Movie_Genre(models.Model):
    movie = models.ForeignKey(Movie)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return " - ".join([str(self.movie), self.genre])
