# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0002_area_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('bonus_base', models.FloatField(verbose_name='\u5956\u91d1\u57fa\u6570')),
                ('job_weight', models.FloatField(verbose_name='\u804c\u52a1\u6743\u6570')),
                ('sale_target', models.FloatField(verbose_name='\u9500\u552e\u6307\u6807')),
                ('exam_target', models.FloatField(verbose_name='\u8003\u6838\u6307\u6807')),
                ('profit_target', models.FloatField(default=0, verbose_name='\u5229\u6da6\u8fbe\u6210\u6307\u6807')),
            ],
            options={
                'db_table': 'perf_job',
                'verbose_name': '\u5c97\u4f4d\u7ba1\u7406',
                'verbose_name_plural': '\u5c97\u4f4d\u7ba1\u7406',
            },
        ),
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': '\u5730\u533a\u7ba1\u7406', 'verbose_name_plural': '\u5730\u533a\u7ba1\u7406'},
        ),
        migrations.AlterModelTable(
            name='area',
            table='perf_area',
        ),
    ]
