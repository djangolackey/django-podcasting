# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def move_enclosure_fk(apps, schema_editor):
  Enclosure = apps.get_model('podcasting', 'Enclosure')
  Episode = apps.get_model('podcasting', 'Episode')
  for enclosure in Enclosure.objects.all():
    episode = Episode.objects.get(id=enclosure.episode.id);
    episode.enclosure = enclosure
    episode.save()

class Migration(migrations.Migration):

    dependencies = [
        ('podcasting', '0002_auto_20140909_0044'),
    ]

    operations = [
        migrations.RunPython(move_enclosure_fk),

        migrations.RemoveField(
            model_name='enclosure',
            name='episode',
        ),

    ]
