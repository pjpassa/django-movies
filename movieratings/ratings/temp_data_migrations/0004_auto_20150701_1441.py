# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv

from django.db import models, migrations

from ratings.models import Movie, Tag, Rater

def import_tags(apps, schema_editor):
    with open("../ml-20m/tags.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            userId = int(row["userId"])
            movie = Movie.objects.get(id=int(row["movieId"]))
            tag = row["tag"]
            timestamp = int(row["timestamp"])
            tagger = Rater.objects.get_or_create(rater=userId, id=userId)[0]
            Tag.objects.create(movie=movie, tag=tag, timestamp=timestamp, rater=tagger)

class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20150701_1358'),
    ]

    operations = [
        migrations.RunPython(import_tags),
    ]
