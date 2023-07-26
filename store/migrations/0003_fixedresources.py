# Generated by Django 4.2.1 on 2023-07-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_usage_function'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('damage', models.PositiveIntegerField()),
                ('report_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
