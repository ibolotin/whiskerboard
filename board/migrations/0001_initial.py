# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import colorfield.fields
from randomslugfield import RandomSlugField


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', RandomSlugField(length=7)),
            ],
            options={
                'ordering': ('severity',),
                'verbose_name_plural': 'statuses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('incident', models.ForeignKey(
                    related_name='events',
                    to='board.Incident',
                    null=True)),
                ('message', models.TextField()),
                ('start', models.DateTimeField(default=datetime.datetime.now)),
                ('informational', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-start',),
                'get_latest_by': 'start',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=255)),
                ('category', models.ForeignKey(
                    related_name='services',
                    to='board.Category',
                    null=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=255)),
                ('severity', models.IntegerField(
                    choices=[(10, b'NORMAL'),
                             (30, b'WARNING'),
                             (40, b'ERROR'),
                             (50, b'CRITICAL')])),
                ('image', models.CharField(max_length=100)),
                ('color', colorfield.fields.ColorField(max_length=10)),
            ],
            options={
                'ordering': ('severity',),
                'verbose_name_plural': 'statuses',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='service',
            field=models.ForeignKey(related_name='events', to='board.Service'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.ForeignKey(related_name='events', to='board.Status'),
            preserve_default=True,
        ),
    ]
