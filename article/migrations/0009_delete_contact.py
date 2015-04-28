# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20150426_1333'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
