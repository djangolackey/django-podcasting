# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcasting', '0003_auto_20140909_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enclosure',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='show',
        ),
        migrations.RemoveField(
            model_name='show',
            name='site',
        ),
    ]
