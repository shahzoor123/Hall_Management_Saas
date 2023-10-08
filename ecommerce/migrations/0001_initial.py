# Generated by Django 4.2.1 on 2023-10-06 16:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('event_time', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EventSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.IntegerField(null=True, unique=True)),
                ('sr', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('Confirm', 'Confirm'), ('Tentative ', 'Tentative')], default='Tentative ', max_length=10)),
                ('event_timing', models.CharField(choices=[('Day', 'Day'), ('Night ', 'Night')], default='Night ', max_length=10)),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('event_date', models.DateField()),
                ('no_of_people', models.IntegerField(null=True)),
                ('location', models.CharField(blank=True, default='Hall', max_length=10)),
                ('setup', models.CharField(choices=[('Normal', 'Normal'), ('Delux', 'Delux'), ('VIP', 'VIP')], default='Delux', max_length=10)),
                ('deals', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=200)),
                ('stage_charges', models.IntegerField(default=0, null=True)),
                ('entry_charges', models.IntegerField(default=0, null=True)),
                ('gents', models.IntegerField(default=0)),
                ('ladies', models.IntegerField(default=0)),
                ('customer_number', models.BigIntegerField()),
                ('per_head', models.IntegerField(null=True)),
                ('extra_charges', models.IntegerField()),
                ('food_menu', models.CharField(max_length=200)),
                ('detials', models.TextField()),
                ('total_menu', models.IntegerField(default=0)),
                ('payment_details', models.TextField()),
                ('payment_count', models.IntegerField(default=0, editable=False)),
                ('total_amount', models.IntegerField(editable=False, null=True)),
                ('recieved_amount', models.IntegerField(null=True)),
                ('remaining_amount', models.IntegerField(editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyKitchenexpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('payment_details', models.TextField(max_length=300)),
                ('mutton', models.CharField(max_length=50)),
                ('chicken', models.CharField(max_length=50)),
                ('beef', models.CharField(max_length=50)),
                ('rice', models.CharField(max_length=50)),
                ('dahi', models.CharField(max_length=50)),
                ('doodh', models.CharField(max_length=50)),
                ('sabzi', models.CharField(max_length=50)),
                ('fruits', models.CharField(max_length=50)),
                ('khoya_cream_paneer', models.CharField(max_length=50)),
                ('dry_fruits', models.CharField(max_length=50)),
                ('oil', models.CharField(max_length=50)),
                ('other_items_bill', models.CharField(max_length=50)),
                ('other_items_desc', models.CharField(max_length=50)),
                ('total_bill', models.CharField(max_length=50)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.eventsale')),
            ],
        ),
        migrations.CreateModel(
            name='EventExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pakwan_bill', models.IntegerField(blank=True, default=0)),
                ('electicity', models.IntegerField(blank=True, default=0)),
                ('naan_qty', models.IntegerField(blank=True, default=0)),
                ('naan_bill', models.IntegerField(blank=True, default=0, editable=False)),
                ('cold_drink', models.IntegerField(blank=True, default=0)),
                ('cold_drink_bill', models.IntegerField(blank=True, default=0, editable=False)),
                ('water', models.IntegerField(blank=True, default=0)),
                ('water_bill', models.IntegerField(blank=True, default=0, editable=False)),
                ('bbq_kg_qty', models.IntegerField(blank=True, default=0)),
                ('bbq_price', models.IntegerField(blank=True, default=0, editable=False)),
                ('diesel_ltr', models.IntegerField(blank=True, default=0)),
                ('no_of_waiters', models.IntegerField(blank=True, default=0)),
                ('waiters_bill', models.IntegerField(blank=True, default=0, editable=False)),
                ('stuff_bill', models.IntegerField(blank=True, default=0, editable=False)),
                ('dhobi', models.IntegerField(blank=True, default=0)),
                ('other_expense', models.IntegerField(blank=True, default=0)),
                ('other_expense_detals', models.TextField(blank=True)),
                ('setup_bill', models.IntegerField(blank=True, default=0)),
                ('decor', models.CharField(blank=True, max_length=200)),
                ('decor_bill', models.IntegerField(blank=True, default=0)),
                ('total_expense', models.IntegerField(blank=True, editable=False)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.eventsale')),
            ],
        ),
    ]
