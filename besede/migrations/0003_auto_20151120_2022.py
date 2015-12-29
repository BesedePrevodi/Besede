# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('besede', '0002_auto_20151015_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='beseda',
            name='opis',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='sklop',
            name='nivo',
            field=models.ForeignKey(to='besede.Nivo'),
        ),
    ]
