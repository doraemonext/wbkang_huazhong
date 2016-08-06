# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0006_staff_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='has_trial',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5b58\u5728\u8bd5\u7528\u671f'),
        ),
        migrations.AddField(
            model_name='job',
            name='trial_days',
            field=models.IntegerField(default=180, verbose_name='\u8bd5\u7528\u671f\u65f6\u957f(\u5929)'),
        ),
        migrations.AlterField(
            model_name='area',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='\u7236\u5730\u533a', blank=True, to='perf.Area', null=True),
        ),
    ]
