from django.db import models


# Create your models here.
class Rater(models.Model):
    rater = models.IntegerField()

    def __str__(self):
        return str(self.rater)


class Movie(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


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
    rating = models.IntegerField()
    timestamp = models.IntegerField()

    def __str__(self):
        return " - ".join([str(self.movie), str(self.rating)])


class Movie_Genre(models.Model):
    movie = models.ForeignKey(Movie)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return " - ".join([str(self.movie), self.genre])