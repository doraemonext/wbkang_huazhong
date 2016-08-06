# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0005_auto_20160806_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='status',
            field=models.IntegerField(default=0, verbose_name='\u5458\u5de5\u72b6\u6001', choices=[(0, '\u5728\u804c'), (1, '\u79bb\u804c')]),
            preserve_default=False,
        ),
    ]
