# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Email',
            field=models.EmailField(max_length=254, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='Name',
            field=models.CharField(max_length=30, default=datetime.datetime(2015, 9, 8, 1, 59, 53, 915373, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
