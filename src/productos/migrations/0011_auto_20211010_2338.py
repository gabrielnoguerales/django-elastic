# Generated by Django 3.2.8 on 2021-10-10 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0010_auto_20211010_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='descuento',
            name='titulo',
            field=models.CharField(default='ChangeMe', max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
