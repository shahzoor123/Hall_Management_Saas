# Generated by Django 4.2.1 on 2023-07-26 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructionAndRepair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_for', models.CharField(max_length=200)),
                ('details', models.CharField(blank=True, max_length=300)),
                ('amount', models.IntegerField(default=0)),
                ('on_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DailyExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_type', models.CharField(choices=[('Cards', 'Cards'), ('Internet Bill', 'Internet Bill'), ('Tea', 'Tea'), ('Utility Bills', 'Utility Bills'), ('Food', 'Food'), ('Other Expenses', 'Others Expenses')], max_length=20)),
                ('details', models.CharField(blank=True, max_length=300)),
                ('amount', models.IntegerField(default=0)),
                ('on_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OtherExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_type', models.CharField(choices=[('Rents', 'Rents'), ('Taxes', 'Taxes'), ('Online Expense', 'Online Expense'), ('Other Expense', 'Other Expense')], max_length=20)),
                ('details', models.CharField(blank=True, max_length=300)),
                ('amount', models.IntegerField(default=0)),
                ('on_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_type', models.CharField(choices=[('Guards', 'Guards'), ('Marquee Staff', 'Marquee Staff'), ('Office Staff', 'Office Staff')], max_length=20)),
                ('details', models.CharField(blank=True, max_length=300)),
                ('amount', models.IntegerField(default=0)),
                ('on_date', models.DateField()),
            ],
        ),
    ]