# Generated by Django 4.2.1 on 2023-06-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0018_alter_eventsale_bill_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsale',
            name='bill_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='eventsale',
            name='customer_number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='eventsale',
            name='detials',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='eventsale',
            name='event_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='eventsale',
            name='extra_charges',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='eventsale',
            name='food_menu',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='eventsale',
            name='recieved_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eventsale',
            name='remaining_amount',
            field=models.IntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='eventsale',
            name='total_amount',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]
