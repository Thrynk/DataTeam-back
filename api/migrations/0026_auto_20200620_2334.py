# Generated by Django 3.0.5 on 2020-06-20 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_prediction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prediction',
            old_name='player_1_proba',
            new_name='player1_proba',
        ),
        migrations.RenameField(
            model_name='prediction',
            old_name='player_2_proba',
            new_name='player2_proba',
        ),
    ]
