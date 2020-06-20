# Generated by Django 3.0.5 on 2020-06-20 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20200619_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_1_proba', models.DecimalField(decimal_places=4, max_digits=6)),
                ('player_2_proba', models.DecimalField(decimal_places=4, max_digits=6)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_id', to='api.Match')),
                ('player1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1_id', to='api.TennisPlayer')),
                ('player2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2_id', to='api.TennisPlayer')),
            ],
        ),
    ]
