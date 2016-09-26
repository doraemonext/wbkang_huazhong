# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0037_auto_20160926_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonushistory',
            name='perf_bonus',
            field=models.FloatField(default=0, verbose_name='\u7ee9\u6548\u5956\u91d1'),
        ),
    ]
