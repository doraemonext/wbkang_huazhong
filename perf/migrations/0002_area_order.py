# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
