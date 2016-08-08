# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0018_remove_area_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u8be6\u7ec6\u540d\u79f0')),
                ('job', models.ForeignKey(verbose_name='\u5c97\u4f4d', to='perf.Job')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'perf_job_match',
                'verbose_name': '\u5c97\u4f4d\u540d\u79f0\u7ba1\u7406',
                'verbose_name_plural': '\u5c97\u4f4d\u540d\u79f0\u7ba1\u7406',
            },
        ),
    ]
