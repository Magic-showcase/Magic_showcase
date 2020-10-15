# Generated by Django 3.1.2 on 2020-10-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Seccion', models.CharField(max_length=50)),
                ('Contenido', models.CharField(max_length=50)),
                ('Precio', models.IntegerField()),
                ('Imagen', models.ImageField(upload_to='')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]