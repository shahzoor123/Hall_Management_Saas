# Generated by Django 4.2.1 on 2023-06-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0021_alter_eventsale_event_timing_alter_eventsale_setup_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsale',
            name='deals',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
