# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0034_job_is_grass_roots'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDataImport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to='/Users/Doraemonext/Project/wb/wbkang/media', verbose_name='Excel \u6587\u4ef6')),
                ('imported', models.BooleanField(default=False, verbose_name='\u662f\u5426\u6210\u529f\u5bfc\u5165')),
                ('message', models.TextField(default='', verbose_name='\u8bf4\u660e\u4fe1\u606f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0a\u4f20\u65e5\u671f')),
            ],
            options={
                'db_table': 'perf_job_data_import',
                'verbose_name': '\u5c97\u4f4d\u6570\u636e\u5bfc\u5165',
                'verbose_name_plural': '\u5c97\u4f4d\u6570\u636e\u5bfc\u5165',
            },
        ),
    ]
