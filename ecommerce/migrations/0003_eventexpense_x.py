# Generated by Django 4.2.1 on 2023-10-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_alter_eventexpense_expense_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventexpense',
            name='x',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
