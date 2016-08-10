# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0028_auto_20160810_0208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='area',
        ),
        migrations.AddField(
            model_name='staff',
            name='area_weight',
            field=models.FloatField(default=0, verbose_name='\u5730\u533a\u6743\u91cd'),
        ),
        migrations.DeleteModel(
            name='Area',
        ),
    ]
