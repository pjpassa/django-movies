# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20150630_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('genres', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('user_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('movie', models.ForeignKey(to='ratings.Movie')),
                ('user', models.ForeignKey(to='ratings.Rater')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('tag', models.CharField(max_length=150)),
                ('timestamp', models.IntegerField()),
                ('movie', models.ForeignKey(to='ratings.Movie')),
                ('user', models.ForeignKey(to='ratings.Rater')),
            ],
        ),
        migrations.RenameField(
            model_name='link',
            old_name='imdbId',
            new_name='imdb',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='tmdbId',
            new_name='tmdb',
        ),
        migrations.RemoveField(
            model_name='link',
            name='movieId',
        ),
        migrations.AddField(
            model_name='link',
            name='id',
            field=models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID', default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='movie',
            field=models.ForeignKey(to='ratings.Movie', default=-1),
            preserve_default=False,
        ),
    ]
