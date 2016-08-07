# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0015_auto_20160807_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='trial_bonus_base',
            field=models.FloatField(default=0, help_text='\u4ec5\u5728\u5b58\u5728\u8bd5\u7528\u671f\u65f6\u6709\u6548', verbose_name='\u8bd5\u7528\u671f\u5956\u91d1\u57fa\u6570(\u5143)'),
        ),
        migrations.AddField(
            model_name='job',
            name='trial_job_weight',
            field=models.FloatField(default=0, help_text='\u4ec5\u5728\u5b58\u5728\u8bd5\u7528\u671f\u65f6\u6709\u6548', verbose_name='\u8bd5\u7528\u671f\u804c\u52a1\u6743\u6570'),
        ),
    ]
