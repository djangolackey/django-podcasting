# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('podcasting', '0002_auto_20140914_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='published',
            field=models.DateTimeField(null=True, verbose_name='published', blank=True),
        ),
    ]
