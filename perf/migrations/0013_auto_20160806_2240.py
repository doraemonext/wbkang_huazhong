# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0012_bonushistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bonushistory',
            old_name='sfa_percent',
            new_name='sfa_reach',
        ),
    ]
