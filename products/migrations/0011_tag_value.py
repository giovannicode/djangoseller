# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='value',
            field=models.CharField(default='', max_length=b'30'),
            preserve_default=False,
        ),
    ]
