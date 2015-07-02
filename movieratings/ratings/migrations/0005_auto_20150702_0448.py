# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv

from django.db import models, migrations
from ratings.models import Movie, Link


def import_links(apps, schema_editor):
    with open("../ml-20m/links.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            movie = Movie.objects.get(id=int(row["movieId"]))
            imdbId = row["imdbId"]
            tmdbId = row["tmdbId"]
            Link.objects.create(movie=movie, imdb=imdbId, tmdb=tmdbId)


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_auto_20150701_1630'),
    ]

    operations = [
        migrations.RunPython(import_links)
    ]
