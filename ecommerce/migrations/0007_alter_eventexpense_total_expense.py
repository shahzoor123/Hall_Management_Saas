# Generated by Django 4.2.1 on 2023-10-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_merge_20231019_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventexpense',
            name='total_expense',
            field=models.IntegerField(blank=True, editable=False),
        ),
    ]
