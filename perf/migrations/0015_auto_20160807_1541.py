# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0014_auto_20160807_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonushistory',
            name='area_weight',
            field=models.FloatField(default=0, verbose_name='\u5730\u533a\u6743\u6570'),
        ),
        migrations.AddField(
            model_name='bonushistory',
            name='bonus_base',
            field=models.FloatField(default=0, verbose_name='\u5956\u91d1\u57fa\u6570(\u5143)'),
        ),
        migrations.AddField(
            model_name='bonushistory',
            name='job_name',
            field=models.CharField(default='', max_length=100, verbose_name='\u5c97\u4f4d\u540d\u79f0'),
        ),
        migrations.AddField(
            model_name='bonushistory',
            name='job_weight',
            field=models.FloatField(default=0, verbose_name='\u804c\u52a1\u6743\u6570'),
        ),
        migrations.AddField(
            model_name='bonushistory',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='openid',
            field=models.CharField(default='', help_text='\u4fee\u6539\u6b64\u5904\u5c06\u5bfc\u81f4\u539f\u7ed1\u5b9a\u65e0\u6548', max_length=255, verbose_name='\u5fae\u4fe1\u7ed1\u5b9aID', blank=True),
        ),
    ]
