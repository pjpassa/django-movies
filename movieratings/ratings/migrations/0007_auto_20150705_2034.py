# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from statistics import mean

from django.db import models, migrations
from ratings.models import Movie, Rating


def average_ratings(apps, schema_editor):
    for movie in Movie.objects.all():
        ratings = [rating.rating for rating in Rating.objects.filter(movie=movie)]
        if ratings:
            movie.average_rating = mean(ratings)
            movie.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0006_movie_average_ratings'),
    ]

    operations = [
        migrations.RunPython(average_ratings)
    ]
