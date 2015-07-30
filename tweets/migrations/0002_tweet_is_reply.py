# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='is_reply',
            field=models.BooleanField(default=False, verbose_name=True),
            preserve_default=False,
        ),
    ]
