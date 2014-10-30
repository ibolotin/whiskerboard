# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_initial_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='url',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
