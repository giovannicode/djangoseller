# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='red', max_length=30, choices=[(b'red', b'red'), (b'orange', b'orange'), (b'yellow', b'yellow'), (b'green', b'green'), (b'cyan', b'cyan'), (b'blue', b'blue'), (b'purple', b'purple'), (b'pink', b'pink'), (b'brown', b'brown'), (b'gold', b'gold'), (b'black', b'black'), (b'gray', b'gray'), (b'white', b'white')]),
            preserve_default=False,
        ),
    ]
