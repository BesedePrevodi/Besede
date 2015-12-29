# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beseda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slovensko', models.CharField(max_length=100)),
                ('anglesko', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sklop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ime_sklopa', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='beseda',
            name='sklop',
            field=models.ForeignKey(to='besede.Sklop'),
        ),
    ]
