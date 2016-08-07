# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0017_auto_20160807_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='order',
        ),
    ]
