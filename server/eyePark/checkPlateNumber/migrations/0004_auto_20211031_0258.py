# Generated by Django 3.2.8 on 2021-10-31 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkPlateNumber', '0003_auto_20211031_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='id',
        ),
        migrations.AlterField(
            model_name='car',
            name='license_plate',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
