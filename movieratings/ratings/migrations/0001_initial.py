# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('imdb', models.CharField(max_length=7)),
                ('tmdb', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(to='ratings.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('rater', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('timestamp', models.IntegerField()),
                ('movie', models.ForeignKey(to='ratings.Movie')),
                ('rater', models.ForeignKey(to='ratings.Rater')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tag', models.CharField(max_length=150)),
                ('timestamp', models.IntegerField()),
                ('movie', models.ForeignKey(to='ratings.Movie')),
                ('rater', models.ForeignKey(to='ratings.Rater')),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='movie',
            field=models.ForeignKey(to='ratings.Movie'),
        ),
    ]
