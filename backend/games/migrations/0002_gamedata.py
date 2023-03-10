# Generated by Django 4.1.7 on 2023-02-26 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GameData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "away_team_players",
                    models.ManyToManyField(
                        related_name="away_team_players", to="games.player"
                    ),
                ),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="game",
                        to="games.game",
                    ),
                ),
                (
                    "home_team_players",
                    models.ManyToManyField(
                        related_name="home_team_players", to="games.player"
                    ),
                ),
            ],
        ),
    ]
