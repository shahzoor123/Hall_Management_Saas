# Generated by Django 4.2.7 on 2023-12-10 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0013_mykitchenexpense_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='sale_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.eventsale'),
        ),
    ]