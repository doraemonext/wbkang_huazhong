# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0016_auto_20160807_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='trial_bonus_base',
        ),
        migrations.RemoveField(
            model_name='job',
            name='trial_job_weight',
        ),
        migrations.AddField(
            model_name='job',
            name='trial_exam_target',
            field=models.FloatField(default=0, help_text='\u4ec5\u5728\u5b58\u5728\u8bd5\u7528\u671f\u65f6\u6709\u6548, \u53d6\u503c\u8303\u56f4 0 - 1', verbose_name='\u8bd5\u7528\u671f\u8003\u6838\u6307\u6807'),
        ),
        migrations.AddField(
            model_name='job',
            name='trial_sale_target',
            field=models.FloatField(default=0, help_text='\u4ec5\u5728\u5b58\u5728\u8bd5\u7528\u671f\u65f6\u6709\u6548, \u53d6\u503c\u8303\u56f4 0 - 1', verbose_name='\u8bd5\u7528\u671f\u9500\u552e\u6307\u6807'),
        ),
    ]
