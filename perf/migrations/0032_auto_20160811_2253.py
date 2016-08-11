# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0031_auto_20160811_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='identifier',
            field=models.CharField(max_length=100, verbose_name='\u5ba2\u6237\u4ee3\u7801'),
        ),
    ]
