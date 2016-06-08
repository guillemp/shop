# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160607_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='zip',
            new_name='zipcode',
        ),
        migrations.AlterField(
            model_name='address',
            name='address_2',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='company',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
