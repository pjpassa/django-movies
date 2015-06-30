# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('movieId', models.IntegerField(primary_key=True, serialize=False)),
                ('imdbId', models.CharField(max_length=7)),
                ('tmdbId', models.IntegerField()),
            ],
        ),
    ]
