# Generated by Django 4.2.2 on 2023-06-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantitas', '0002_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre'),
        ),
    ]