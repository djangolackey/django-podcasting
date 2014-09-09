# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcasting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enclosure',
            options={'ordering': ('mime',), 'verbose_name': 'Enclosure', 'verbose_name_plural': 'Enclosures'},
        ),
        migrations.AddField(
            model_name='episode',
            name='enclosure',
            field=models.ForeignKey(default=0, verbose_name='enclosure', to='podcasting.Enclosure'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episode',
            name='shows',
            field=models.ManyToManyField(to=b'podcasting.Show', verbose_name='Podcasts'),
        ),
        migrations.AddField(
            model_name='show',
            name='sites',
            field=models.ManyToManyField(to=b'sites.Site', verbose_name='Sites'),
        ),
        migrations.AlterUniqueTogether(
            name='enclosure',
            unique_together=None,
        ),
    ]
