 
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticketAgent', '0002_auto_20190601_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='full_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='signup',
            name='surname',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]
