# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0038_bonushistory_perf_bonus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonushistory',
            name='perf_bonus',
        ),
        migrations.AlterField(
            model_name='bonushistory',
            name='group',
            field=models.CharField(default='', max_length=100, verbose_name='\u7ec4\u522b', blank=True),
        ),
        migrations.AlterField(
            model_name='bonushistory',
            name='place',
            field=models.CharField(default='', max_length=100, verbose_name='\u6240\u522b', blank=True),
        ),
    ]
