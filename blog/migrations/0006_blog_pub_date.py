# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150908_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 8, 3, 49, 39, 401727, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
