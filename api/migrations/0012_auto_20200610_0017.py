# Generated by Django 3.0.5 on 2020-06-09 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200608_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tennisplayerstats',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.TennisPlayer'),
        ),
    ]
