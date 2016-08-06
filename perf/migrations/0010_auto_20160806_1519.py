# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0009_auto_20160806_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffTarget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(verbose_name='\u5e74')),
                ('month', models.IntegerField(verbose_name='\u6708')),
                ('target', models.FloatField(verbose_name='\u4e2a\u4eba\u76ee\u6807(\u5143)')),
            ],
            options={
                'ordering': ['-year', '-month', '-id'],
                'db_table': 'perf_staff_target',
                'verbose_name': '\u5458\u5de5\u76ee\u6807\u7ba1\u7406',
                'verbose_name_plural': '\u5458\u5de5\u76ee\u6807\u7ba1\u7406 ',
            },
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-id'], 'verbose_name': '\u5ba2\u6237\u4fe1\u606f\u7ba1\u7406', 'verbose_name_plural': '\u5ba2\u6237\u4fe1\u606f\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='clienttarget',
            options={'ordering': ['-year', '-month', '-id'], 'verbose_name': '\u5ba2\u6237\u76ee\u6807\u7ba1\u7406', 'verbose_name_plural': '\u5ba2\u6237\u76ee\u6807\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-id'], 'verbose_name': '\u5c97\u4f4d\u7ba1\u7406', 'verbose_name_plural': '\u5c97\u4f4d\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['-id'], 'verbose_name': '\u5458\u5de5\u7ba1\u7406', 'verbose_name_plural': '\u5458\u5de5\u7ba1\u7406'},
        ),
        migrations.AddField(
            model_name='stafftarget',
            name='client_target',
            field=models.ForeignKey(verbose_name='\u5ba2\u6237\u76ee\u6807', to='perf.ClientTarget'),
        ),
        migrations.AddField(
            model_name='stafftarget',
            name='staff',
            field=models.ForeignKey(verbose_name='\u5458\u5de5', to='perf.Staff'),
        ),
    ]
