# Generated by Django 4.2.1 on 2023-05-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_alter_eventexpense_naan_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventexpense',
            name='cold_drink_bill',
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='eventexpense',
            name='stuff_bill',
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
    ]
