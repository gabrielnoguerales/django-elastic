# Generated by Django 3.2.8 on 2021-10-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_alter_descuento_codigo_descuento'),
    ]

    operations = [
        migrations.AddField(
            model_name='descuento',
            name='notas',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='descuento',
            name='titulo',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
