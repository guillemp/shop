# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160607_1500'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Zone',
            new_name='Region',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='province',
            new_name='region',
        ),
    ]
