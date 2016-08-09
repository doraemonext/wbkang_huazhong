# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0025_auto_20160809_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffdataimport',
            name='error_message',
        ),
        migrations.AddField(
            model_name='staffdataimport',
            name='message',
            field=models.CharField(default='', max_length=255, verbose_name='\u8bf4\u660e\u4fe1\u606f'),
        ),
    ]
