# Generated by Django 5.1.4 on 2025-01-25 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BusCompany', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='bus_id',
            new_name='bus',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='rout_id',
            new_name='rout',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='user_id',
            new_name='user',
        ),
    ]
