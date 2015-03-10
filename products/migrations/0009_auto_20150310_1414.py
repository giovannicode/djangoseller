# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20150310_1405'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Filter',
            new_name='Tag',
        ),
    ]
