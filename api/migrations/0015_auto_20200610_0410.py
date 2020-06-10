# Generated by Django 3.0.5 on 2020-06-10 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200610_0308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tennisplayerstats',
            old_name='others_2st_won',
            new_name='others_1st_won',
        ),
        migrations.AddField(
            model_name='tennisplayerstats',
            name='serve_points',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='surface',
            field=models.CharField(max_length=15),
        ),
    ]
