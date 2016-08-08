# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0019_jobmatch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobmatch',
            options={'ordering': ['name'], 'verbose_name': '\u5c97\u4f4d\u540d\u79f0\u7ba1\u7406', 'verbose_name_plural': '\u5c97\u4f4d\u540d\u79f0\u7ba1\u7406'},
        ),
        migrations.AlterField(
            model_name='jobmatch',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='\u8be6\u7ec6\u540d\u79f0'),
        ),
    ]
