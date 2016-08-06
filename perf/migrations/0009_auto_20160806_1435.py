# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0008_auto_20160806_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientTarget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(verbose_name='\u5e74')),
                ('month', models.IntegerField(verbose_name='\u6708')),
                ('target', models.FloatField(verbose_name='\u5ba2\u6237\u76ee\u6807\u91d1\u989d(\u5143)')),
            ],
            options={
                'ordering': ['year', 'month', 'id'],
                'db_table': 'perf_client_target',
                'verbose_name': '\u5ba2\u6237\u76ee\u6807\u7ba1\u7406',
                'verbose_name_plural': '\u5ba2\u6237\u76ee\u6807\u7ba1\u7406',
            },
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['id'], 'verbose_name': '\u5ba2\u6237\u4fe1\u606f\u7ba1\u7406', 'verbose_name_plural': '\u5ba2\u6237\u4fe1\u606f\u7ba1\u7406'},
        ),
        migrations.AddField(
            model_name='clienttarget',
            name='client',
            field=models.ForeignKey(verbose_name='\u5ba2\u6237', to='perf.Client'),
        ),
    ]
