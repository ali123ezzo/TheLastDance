# Generated by Django 5.1.4 on 2025-01-25 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusCompany', '0004_alter_schedule_rout_alter_ticket_booking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='bus_id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
