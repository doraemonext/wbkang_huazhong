# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0022_auto_20160809_0116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataimport',
            options={'ordering': ['-year', '-month'], 'verbose_name': '\u6570\u636e\u5bfc\u5165', 'verbose_name_plural': '\u6570\u636e\u5bfc\u5165'},
        ),
        migrations.AlterField(
            model_name='staff',
            name='identifier',
            field=models.CharField(unique=True, max_length=100, verbose_name='\u5458\u5de5\u53f7'),
        ),
    ]
