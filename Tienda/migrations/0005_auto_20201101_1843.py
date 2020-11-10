# Generated by Django 3.1.2 on 2020-11-01 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tienda', '0004_auto_20201101_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='envio',
            name='Numero',
        ),
        migrations.AddField(
            model_name='envio',
            name='Cliente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.CreateModel(
            name='Venta_descrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField()),
                ('Precio_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('Producto', models.ManyToManyField(to='Tienda.Producto')),
            ],
            options={
                'verbose_name': 'Venta_descrip',
                'verbose_name_plural': 'Venta_descrip',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Precio_IVA', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Costo_total', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('Venta_desc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Tienda.venta_descrip')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.AddField(
            model_name='envio',
            name='Venta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Tienda.venta'),
        ),
    ]
