 
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticketAgent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='repeatPassword',
        ),
        migrations.AddField(
            model_name='signup',
            name='repeat_password',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=60),
        ),
    ]
