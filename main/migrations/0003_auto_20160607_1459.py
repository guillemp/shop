# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160605_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('country', models.ForeignKey(to='main.Country')),
            ],
        ),
        migrations.RenameField(
            model_name='address',
            old_name='postcode',
            new_name='zip',
        ),
        migrations.AddField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.ForeignKey(default=0, to='main.Zone'),
            preserve_default=False,
        ),
    ]
