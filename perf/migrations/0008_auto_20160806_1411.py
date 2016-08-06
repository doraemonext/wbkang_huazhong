# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0007_auto_20160806_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=100, verbose_name='\u5ba2\u6237\u4ee3\u7801')),
                ('name', models.CharField(max_length=100, verbose_name='\u5ba2\u6237\u540d\u79f0')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'perf_client',
                'verbose_name': '\u5ba2\u6237\u7ba1\u7406',
                'verbose_name_plural': '\u5ba2\u6237\u7ba1\u7406',
            },
        ),
        migrations.AlterField(
            model_name='job',
            name='has_trial',
            field=models.BooleanField(default=False, verbose_name='\u5b58\u5728\u8bd5\u7528\u671f'),
        ),
        migrations.AlterField(
            model_name='job',
            name='trial_days',
            field=models.IntegerField(default=180, help_text='\u4ec5\u5728\u5b58\u5728\u8bd5\u7528\u671f\u65f6\u6709\u6548', verbose_name='\u8bd5\u7528\u671f\u65f6\u957f(\u5929)'),
        ),
    ]
