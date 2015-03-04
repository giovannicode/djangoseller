# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_cart_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='session_key',
            field=models.CharField(max_length=40, unique=True, null=True),
            preserve_default=True,
        ),
    ]
