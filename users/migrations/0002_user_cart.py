# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_remove_cart_user'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.OneToOneField(default=1, to='carts.Cart'),
            preserve_default=False,
        ),
    ]
