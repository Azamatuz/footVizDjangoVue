from django.db import models


# Create your models here.
# Soccer stats



class Stat(models.Model):
    #['Goals', 'Assists', 'Shots', 'SCA', 'GCA', 'Touches', 'Passes', 'PrgP',
    #   'Carries', 'PrgC', 'Tackled', 'Interceptions', 'Blocks', 'Total',
    #   'Attack', 'Defence']
    assists = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    shots = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sca = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    touches = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    passes = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    carries = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tackled = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    interceptions = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    blocks = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

class StatSum(models.Model):
    attack = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    defense = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)


class Player(models.Model):
    name = models.CharField(max_length=100)
    stats = models.ManyToManyField(Stat, related_name="stats")
    stats_sum = models.ManyToManyField(StatSum, related_name="stats_sum")

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, related_name="players")

    def __str__(self):
        return self.name


class TeamStats(models.Model):
    team_name = models.CharField(max_length=100)
    stats = models.ManyToManyField(Stat, related_name="team_stats")

class Game(models.Model):
    date = models.DateField()
    home_team_stats = models.ForeignKey(TeamStats, on_delete=models.CASCADE, related_name="home_games")
    away_team_stats = models.ForeignKey(TeamStats, on_delete=models.CASCADE, related_name="away_games")
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_team")





class GameData(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game")
    home_team_players = models.ManyToManyField(Player, related_name="home_team_players")
    away_team_players = models.ManyToManyField(Player, related_name="away_team_players")
