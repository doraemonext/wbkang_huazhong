# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0003_auto_20160806_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=100, verbose_name='\u5458\u5de5\u53f7')),
                ('name', models.CharField(max_length=100, verbose_name='\u59d3\u540d')),
                ('gender', models.IntegerField(verbose_name='\u6027\u522b', choices=[(0, '\u7537'), (1, '\u5973')])),
                ('department', models.CharField(max_length=100, verbose_name='\u90e8\u95e8')),
                ('entry_date', models.DateField(verbose_name='\u5165\u804c\u65e5\u671f')),
                ('cost_center', models.CharField(max_length=100, verbose_name='\u6210\u672c\u4e2d\u5fc3')),
                ('department_desc', models.CharField(max_length=200, verbose_name='\u90e8\u95e8\u63cf\u8ff0')),
                ('cost_center_number', models.CharField(max_length=100, verbose_name='\u6210\u672c\u4e2d\u5fc3\u7801')),
                ('area', models.ForeignKey(verbose_name='\u5730\u533a', to='perf.Area')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'perf_staff',
                'verbose_name': '\u5458\u5de5\u7ba1\u7406',
                'verbose_name_plural': '\u5458\u5de5\u7ba1\u7406',
            },
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['id'], 'verbose_name': '\u5c97\u4f4d\u7ba1\u7406', 'verbose_name_plural': '\u5c97\u4f4d\u7ba1\u7406'},
        ),
        migrations.AddField(
            model_name='staff',
            name='job',
            field=models.ForeignKey(verbose_name='\u5c97\u4f4d', to='perf.Job'),
        ),
    ]
