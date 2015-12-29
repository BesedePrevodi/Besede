# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('besede', '0003_auto_20151120_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beseda',
            old_name='anglesko',
            new_name='beseda',
        ),
        migrations.RenameField(
            model_name='beseda',
            old_name='slovensko',
            new_name='prevod',
        ),
    ]
