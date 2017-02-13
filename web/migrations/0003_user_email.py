# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170212_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=b'', max_length=254),
        ),
    ]
