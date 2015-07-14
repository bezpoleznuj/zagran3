# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20150714_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planarea',
            old_name='planarea_foto_s',
            new_name='planarea_s',
        ),
    ]
