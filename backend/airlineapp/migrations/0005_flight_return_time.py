# Generated by Django 4.0.3 on 2023-06-06 19:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('airlineapp', '0004_city_alter_flight_destination_alter_flight_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='return_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]