# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='user',
            new_name='rater',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='user',
            new_name='rater',
        ),
        migrations.AlterField(
            model_name='link',
            name='tmdb',
            field=models.CharField(max_length=7),
        ),
    ]
