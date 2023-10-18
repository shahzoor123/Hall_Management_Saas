# Generated by Django 4.2.1 on 2023-10-16 20:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_remove_inventory_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
