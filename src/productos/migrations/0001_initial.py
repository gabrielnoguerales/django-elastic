# Generated by Django 3.2.8 on 2021-10-10 13:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('foto', models.ImageField(upload_to='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('acumulable', models.BooleanField(default=False)),
                ('valor_fijo', models.IntegerField(default=0)),
                ('codigo_descuento', models.CharField(max_length=100)),
                ('encontrable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('precio_base', models.FloatField()),
                ('foto', models.ImageField(upload_to='Productos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.discount')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.discount'),
        ),
    ]
