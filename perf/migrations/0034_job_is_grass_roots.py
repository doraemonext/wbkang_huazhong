# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0033_auto_20160811_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_grass_roots',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u4e3a\u57fa\u5c42\u4eba\u5458'),
        ),
    ]
