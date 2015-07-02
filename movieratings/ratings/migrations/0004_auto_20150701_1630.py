# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv

from django.db import models, migrations

from ratings.models import Movie, Rater, Rating


def import_ratings(apps, schema_editor):
    with open("../ml-20m/ratings.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            userId = int(row["userId"])
            movie = Movie.objects.get(id=int(row["movieId"]))
            rating = float(row["rating"])
            timestamp = int(row["timestamp"])
            rater = Rater.objects.get_or_create(rater=userId, id=userId)[0]
            Rating.objects.create(movie=movie, rating=rating, timestamp=timestamp, rater=rater)


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20150701_1612'),
    ]

    operations = [
        migrations.RunPython(import_ratings),
    ]