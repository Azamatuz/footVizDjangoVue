from django.db import models


# Create your models here.
# Soccer stats
class Stat(models.Model):
    assists = models.IntegerField()
    goals = models.IntegerField()
    passes = models.IntegerField()
    blocks = models.IntegerField()


class Player(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    birthday = models.DateField()
    stats = models.ForeignKey(Stat, on_delete=models.CASCADE, related_name="stats")

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, related_name="players")

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateField()
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="home_team"
    )
    away_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="away_team"
    )


class GameData(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game")
    home_team_players = models.ManyToManyField(Player, related_name="home_team_players")
    away_team_players = models.ManyToManyField(Player, related_name="away_team_players")
