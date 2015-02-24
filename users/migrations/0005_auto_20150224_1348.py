# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cart',
            field=models.OneToOneField(null=True, to='carts.Cart'),
            preserve_default=True,
        ),
    ]
