# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('besede', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ime_nivoja', models.CharField(default=b'Nivo', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='sklop',
            name='nivo',
            field=models.ForeignKey(default=0, to='besede.Nivo'),
        ),
    ]
