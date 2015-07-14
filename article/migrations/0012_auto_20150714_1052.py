# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_remove_planhouse_planhouse_foto_s'),
    ]

    operations = [
        migrations.AddField(
            model_name='planarea',
            name='planarea_foto_s',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='planhouse',
            name='planhouse_foto_s',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
