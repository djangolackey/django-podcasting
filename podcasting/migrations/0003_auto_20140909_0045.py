# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def move_enclosure_fk(apps, schema_editor):
  Enclosure = apps.get_model('podcasting', 'Enclosure')
  Episode = apps.get_model('podcasting', 'Episode')
  for enclosure_item in Enclosure.objects.all():
      episode = Episode.objects.get(id=enclosure_item.episode.id);
      episode.enclosure = enclosure_item
      episode.save()

def move_show_site(apps, schema_editor):
  Site = apps.get_model('django.contrib.sites', 'Site')
  Show = apps.get_model('podcasting', 'Show')
  for show_item in Show.objects.all();
      site_item = Site.objects.get(id=show_item.site.id)
      show_item.add(site_item)
      show_item.save()

def move_episode_show(apps, schema_editor):
  Episode = apps.get_model('podcasting', 'Episode')
  Show = apps.get_model('podcasting', 'Show')
  for episode_item in Episode.objects.all();
      show_item = Show.objects.get(id=episode_item.show.id)
      episode_item.add(show_item)
      episode_item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('podcasting', '0002_auto_20140909_0044'),
    ]

    operations = [
        migrations.RunPython(move_enclosure_fk),

        migrations.RunPython(move_show_site),

        migrations.RunPython(move_episode_show),

        migrations.RemoveField(
            model_name='enclosure',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='show',
            name='site',
        ),
        migrations.RemoveField(
            model_name='enclosure',
            name='show',
        ),
    ]
