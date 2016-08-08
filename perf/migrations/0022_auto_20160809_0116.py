# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0021_staff_job_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataImport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(verbose_name='\u5e74')),
                ('month', models.IntegerField(verbose_name='\u6708')),
                ('file', models.FileField(upload_to=b'', verbose_name='Excel \u6587\u4ef6')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0a\u4f20\u65e5\u671f')),
            ],
            options={
                'db_table': 'perf_data_import',
                'verbose_name': '\u6570\u636e\u5bfc\u5165',
                'verbose_name_plural': '\u6570\u636e\u5bfc\u5165',
            },
        ),
        migrations.AlterField(
            model_name='jobmatch',
            name='job',
            field=models.ForeignKey(verbose_name='\u5bf9\u5e94\u5c97\u4f4d', to='perf.Job'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='job_name',
            field=models.CharField(max_length=100, verbose_name='\u5c97\u4f4d\u540d\u79f0', blank=True),
        ),
    ]
