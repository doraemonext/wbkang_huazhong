# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0011_auto_20160806_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(verbose_name='\u5e74')),
                ('month', models.IntegerField(verbose_name='\u6708')),
                ('last_month_reach', models.FloatField(verbose_name='\u4e0a\u6708\u5ba2\u6237\u8fbe\u6210\u7387')),
                ('current_month_reach', models.FloatField(verbose_name='\u672c\u6708\u5ba2\u6237\u8fbe\u6210\u7387')),
                ('sfa_percent', models.FloatField(verbose_name='SFA\u56de\u5355\u8fbe\u6210\u7cfb\u6570\u5360\u6bd4')),
                ('sale_bonus', models.FloatField(verbose_name='\u4e2a\u4eba\u9500\u552e\u5956\u91d1')),
                ('exam_bonus', models.FloatField(verbose_name='\u4e2a\u4eba\u8003\u6838\u5956\u91d1')),
                ('staff', models.ForeignKey(verbose_name='\u5458\u5de5', to='perf.Staff')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'perf_bonus_history',
                'verbose_name': '\u5956\u91d1\u5386\u53f2\u8bb0\u5f55',
                'verbose_name_plural': '\u5956\u91d1\u5386\u53f2\u8bb0\u5f55',
            },
        ),
    ]
