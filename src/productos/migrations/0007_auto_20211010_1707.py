# Generated by Django 3.2.8 on 2021-10-10 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_auto_20211010_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='discount',
            new_name='descuento',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='discount',
            new_name='descuento',
        ),
    ]
