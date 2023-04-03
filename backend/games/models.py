from django.db import models


# Create your models here.
# Soccer stats



class Stat(models.Model):
    shots = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sca = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    touches = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    passes = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    carries = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    press = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tackled = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    interceptions = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    blocks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

class Player(models.Model):
    name = models.CharField(max_length=100)
    stats = models.ManyToManyField(Stat, related_name="stats")

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, related_name="players")

    def __str__(self):
        return self.name


class TeamStats(models.Model):
    date = models.DateField()
    home_team_stats = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team_stats")
    away_team_stats = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_team_stats")
    stats = models.ManyToManyField(Stat, related_name="team_stats")

class Game(models.Model):
    date = models.DateField()
    teams_stats = models.OneToOneField(TeamStats, on_delete=models.CASCADE)
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
