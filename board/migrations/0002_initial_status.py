# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def initial_status(apps, schema_editor):
        Status = apps.get_model("board", "Status")
        Status.objects.bulk_create([
            Status(name="Up", slug="up", css="success", image="tick-circle",
                   severity=10, color="#396", description="The service is up"),
            Status(name="Down", slug="down", css="danger",
                   image="cross-circle", severity=40, color="#FF0000",
                   description="The service is currently down"),
            Status(name="Warning", slug="warning", css="warning",
                   image="exclamation", color="#F29D50", severity=30,
                   description="The service is experiencing problems"),
        ])

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_status),
    ]
