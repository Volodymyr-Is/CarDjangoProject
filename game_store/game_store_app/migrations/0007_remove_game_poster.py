# Generated by Django 5.0.3 on 2024-05-02 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_store_app', '0006_game_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='poster',
        ),
    ]
