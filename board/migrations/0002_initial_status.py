# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def initial_status(apps, schema_editor):
        Status = apps.get_model("board", "Status")
        Status.objects.bulk_create([
            Status(name="Up", slug="up", image="tick-circle", severity=10,
                   description="The service is up"),
            Status(name="Down", slug="down", image="cross-circle", severity=40,
                   description="The service is currently down"),
            Status(name="Warning", slug="warning", image="exclamation",
                   severity=30,
                   description="The service is experiencing problems"),
        ])

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_status),
    ]
