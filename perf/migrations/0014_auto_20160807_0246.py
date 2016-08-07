# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0013_auto_20160806_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='openid',
            field=models.CharField(default='', help_text='\u4fee\u6539\u6b64\u5904\u5c06\u5bfc\u81f4\u539f\u7ed1\u5b9a\u65e0\u6548', max_length=255, verbose_name='\u5fae\u4fe1\u7ed1\u5b9aID'),
        ),
        migrations.AlterField(
            model_name='bonushistory',
            name='current_month_reach',
            field=models.FloatField(help_text='\u53d6\u503c\u8303\u56f4 0 - 1', verbose_name='\u672c\u6708\u5ba2\u6237\u8fbe\u6210\u7387'),
        ),
        migrations.AlterField(
            model_name='bonushistory',
            name='last_month_reach',
            field=models.FloatField(help_text='\u53d6\u503c\u8303\u56f4 0 - 1', verbose_name='\u4e0a\u6708\u5ba2\u6237\u8fbe\u6210\u7387'),
        ),
        migrations.AlterField(
            model_name='bonushistory',
            name='sfa_reach',
            field=models.FloatField(help_text='\u53d6\u503c\u8303\u56f4 0 - 1', verbose_name='SFA\u56de\u5355\u8fbe\u6210\u7cfb\u6570\u5360\u6bd4'),
        ),
        migrations.AlterField(
            model_name='job',
            name='bonus_base',
            field=models.FloatField(verbose_name='\u5956\u91d1\u57fa\u6570(\u5143)'),
        ),
        migrations.AlterField(
            model_name='job',
            name='exam_target',
            field=models.FloatField(help_text='\u53d6\u503c\u8303\u56f4 0 - 1', verbose_name='\u8003\u6838\u6307\u6807'),
        ),
        migrations.AlterField(
            model_name='job',
            name='profit_target',
            field=models.FloatField(default=0, help_text='\u53d6\u503c\u8303\u56f4 0 - 1', verbose_name='\u5229\u6da6\u8fbe\u6210\u6307\u6807'),
        ),
        migrations.AlterField(
            model_name='job',
            name='sale_target',
            field=models.FloatField(help_text='\u53d6\u503c\u8303\u56f4 0 - 1', verbose_name='\u9500\u552e\u6307\u6807'),
        ),
    ]
