# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0024_auto_20160809_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffdataimport',
            name='error_message',
            field=models.CharField(default='', max_length=255, verbose_name='\u5bfc\u5165\u51fa\u9519\u539f\u56e0'),
        ),
        migrations.AddField(
            model_name='staffdataimport',
            name='imported',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u6210\u529f\u5bfc\u5165'),
        ),
    ]
