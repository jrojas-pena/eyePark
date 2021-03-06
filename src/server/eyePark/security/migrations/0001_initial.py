# Generated by Django 3.2.8 on 2021-12-03 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checkPlateNumber', '0004_auto_20211031_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityAlerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='checkPlateNumber.car')),
                ('parking_spot', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='checkPlateNumber.parking_lot')),
            ],
        ),
    ]
