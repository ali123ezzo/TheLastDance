# Generated by Django 5.1.7 on 2025-04-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusCompany', '0018_rename_absuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
