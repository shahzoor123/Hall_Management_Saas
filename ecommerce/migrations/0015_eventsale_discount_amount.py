# Generated by Django 4.2.1 on 2024-01-08 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_event_sale_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsale',
            name='discount_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]