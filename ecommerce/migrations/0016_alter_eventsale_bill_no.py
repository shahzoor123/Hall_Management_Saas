# Generated by Django 4.2.1 on 2023-06-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_alter_eventsale_bill_no_alter_eventsale_no_of_people_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsale',
            name='bill_no',
            field=models.IntegerField(default=0, null=True),
        ),
    ]