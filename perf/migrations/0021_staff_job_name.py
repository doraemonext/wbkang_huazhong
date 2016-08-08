# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0020_auto_20160809_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='job_name',
            field=models.CharField(default='', max_length=100, verbose_name='\u5c97\u4f4d\u8be6\u7ec6\u540d\u79f0'),
            preserve_default=False,
        ),
    ]
