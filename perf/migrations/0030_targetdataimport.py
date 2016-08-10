# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0029_auto_20160810_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetDataImport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(verbose_name='\u5e74')),
                ('month', models.IntegerField(verbose_name='\u6708')),
                ('file', models.FileField(upload_to='/Users/Doraemonext/Project/wb/wbkang/media', verbose_name='Excel \u6587\u4ef6')),
                ('imported', models.BooleanField(default=False, verbose_name='\u662f\u5426\u6210\u529f\u5bfc\u5165')),
                ('message', models.TextField(default='', verbose_name='\u8bf4\u660e\u4fe1\u606f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0a\u4f20\u65e5\u671f')),
            ],
            options={
                'ordering': ['-year', '-month'],
                'db_table': 'perf_target_data_import',
                'verbose_name': '\u76ee\u6807\u6570\u636e\u5bfc\u5165',
                'verbose_name_plural': '\u76ee\u6807\u6570\u636e\u5bfc\u5165',
            },
        ),
    ]
