# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0004_auto_20160806_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='password',
            field=models.CharField(default='', max_length=64, verbose_name='\u5bc6\u7801'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='area',
            field=mptt.fields.TreeForeignKey(verbose_name='\u5730\u533a', to='perf.Area'),
        ),
    ]
