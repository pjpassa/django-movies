# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models, migrations
from ratings.models import Rater


def create_users(apps, schema_editor):
    for rater in Rater.objects.all():
        user = User(username="User{}".format(rater.id))
        user.set_password("password")
        user.save()
        rater.user = user
        rater.save()

class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0008_rater_user'),
    ]

    operations = [
        migrations.RunPython(create_users)
    ]
