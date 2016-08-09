# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0023_auto_20160809_2030'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataImport',
            new_name='StaffDataImport',
        ),
        migrations.AlterModelOptions(
            name='staffdataimport',
            options={'ordering': ['-year', '-month'], 'verbose_name': '\u5458\u5de5\u4fe1\u606f\u5bfc\u5165', 'verbose_name_plural': '\u5458\u5de5\u4fe1\u606f\u5bfc\u5165'},
        ),
        migrations.AlterModelTable(
            name='staffdataimport',
            table='perf_staff_data_import',
        ),
    ]
