# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0035_jobdataimport'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienttarget',
            name='group',
            field=models.CharField(max_length=100, null=True, verbose_name='\u7ec4\u522b', blank=True),
        ),
    ]
