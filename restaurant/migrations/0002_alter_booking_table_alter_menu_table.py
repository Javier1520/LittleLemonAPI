# Generated by Django 5.0.4 on 2024-04-18 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='booking',
            table='Bookings',
        ),
        migrations.AlterModelTable(
            name='menu',
            table='Menu',
        ),
    ]
