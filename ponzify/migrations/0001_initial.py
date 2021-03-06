# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=20)),
                ('amount', models.CharField(default=b'', max_length=10)),
                ('matrix', models.CharField(choices=[(b'2:1', b'2:1'), (b'3:1', b'3:1'), (b'4:1', b'4:1')], default=b'2:1', max_length=10)),
                ('assign', models.CharField(default=b'Auto Assign', max_length=20)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Plans',
            },
        ),
    ]
