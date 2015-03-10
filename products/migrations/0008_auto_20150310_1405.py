# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_filters'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filter',
            old_name='tag',
            new_name='name',
        ),
    ]
