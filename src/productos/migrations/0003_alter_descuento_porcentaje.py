# Generated by Django 3.2.8 on 2021-10-10 14:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_rename_discount_descuento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuento',
            name='porcentaje',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
