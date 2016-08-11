# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0030_targetdataimport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='identifier',
            field=models.CharField(unique=True, max_length=100, verbose_name='\u5ba2\u6237\u4ee3\u7801'),
        ),
    ]
