# Generated by Django 5.0.2 on 2024-03-04 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='name',
            new_name='brand',
        ),
    ]
