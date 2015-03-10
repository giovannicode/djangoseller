# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150309_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='filters',
        ),
    ]
