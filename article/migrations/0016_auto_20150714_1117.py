# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20150714_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planarea',
            old_name='planarea_s',
            new_name='planarea_foto_s',
        ),
        migrations.AddField(
            model_name='planhouse',
            name='planhouse_foto_s',
            field=models.ImageField(upload_to='', default='', blank=True),
        ),
    ]
