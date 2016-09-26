# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0036_clienttarget_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-identifier'], 'verbose_name': '\u5ba2\u6237\u4fe1\u606f\u7ba1\u7406', 'verbose_name_plural': '\u5ba2\u6237\u4fe1\u606f\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['-identifier'], 'verbose_name': '\u5458\u5de5\u7ba1\u7406', 'verbose_name_plural': '\u5458\u5de5\u7ba1\u7406'},
        ),
        migrations.AddField(
            model_name='bonushistory',
            name='add_bonus',
            field=models.FloatField(default=0, verbose_name='\u52a0\u7801\u5956'),
        ),
        migrations.AddField(
            model_name='bonushistory',
            name='group',
            field=models.CharField(default='', max_length=100, verbose_name='\u7ec4\u522b'),
        ),
        migrations.AddField(
            model_name='bonushistory',
            name='leader_adjust',
            field=models.FloatField(default=0, verbose_name='\u4e3b\u7ba1\u8c03\u6574'),
        ),
        migrations.AddField(
            model_name='bonushistory',
            name='other_bonus',
            field=models.FloatField(default=0, verbose_name='\u5176\u4ed6\u5956\u91d1'),
        ),
        migrations.AddField(
            model_name='bonushistory',
            name='place',
            field=models.CharField(default='', max_length=100, verbose_name='\u6240\u522b'),
        ),
        migrations.AddField(
            model_name='bonushistory',
            name='total_bonus',
            field=models.FloatField(default=0, verbose_name='\u5956\u91d1\u5408\u8ba1'),
        ),
        migrations.AddField(
            model_name='bonushistory',
            name='vacation_deduct',
            field=models.FloatField(default=0, verbose_name='\u8bf7\u5047/\u60e9\u5904\u6263\u6b3e'),
        ),
    ]
