# Generated by Django 3.1.2 on 2020-11-23 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '__first__'),
        ('Tutorial', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tutorial',
            new_name='Tutorials',
        ),
    ]
