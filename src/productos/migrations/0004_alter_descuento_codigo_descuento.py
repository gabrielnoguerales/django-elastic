# Generated by Django 3.2.8 on 2021-10-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_descuento_porcentaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuento',
            name='codigo_descuento',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
