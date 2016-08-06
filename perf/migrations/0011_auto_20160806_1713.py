# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0010_auto_20160806_1519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stafftarget',
            options={'ordering': ['-id'], 'verbose_name': '\u5458\u5de5\u76ee\u6807\u7ba1\u7406', 'verbose_name_plural': '\u5458\u5de5\u76ee\u6807\u7ba1\u7406 '},
        ),
        migrations.RemoveField(
            model_name='stafftarget',
            name='month',
        ),
        migrations.RemoveField(
            model_name='stafftarget',
            name='year',
        ),
    ]
