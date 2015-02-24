# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_remove_cart_user'),
        ('users', '0003_remove_user_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.OneToOneField(null=True, to='carts.Cart'),
            preserve_default=True,
        ),
    ]
