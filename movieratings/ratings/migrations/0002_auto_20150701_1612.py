# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv

from django.db import models, migrations

from ratings.models import Movie, Movie_Genre

def import_movies(apps, schema_editor):
    with open("../ml-20m/movies.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            movieId = int(row["movieId"])
            title = row["title"]
            genres = row["genres"].split("|")
            movie = Movie.objects.create(id=movieId, title=title)
            for genre in genres:
                Movie_Genre.objects.create(movie=movie, genre=genre)

class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_movies),
    ]
