# Generated by Django 4.2.1 on 2023-10-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_alter_eventexpense_total_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventexpense',
            name='cold_drink_type',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
