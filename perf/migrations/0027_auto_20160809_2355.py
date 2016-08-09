# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0026_auto_20160809_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdataimport',
            name='message',
            field=models.TextField(default='', verbose_name='\u8bf4\u660e\u4fe1\u606f'),
        ),
    ]
