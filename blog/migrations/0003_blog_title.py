# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150908_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Title',
            field=models.CharField(max_length=30, default=datetime.datetime(2015, 9, 8, 2, 6, 38, 849403, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
