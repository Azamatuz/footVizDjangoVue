from django.db import models


# Create your models here.
# Soccer stats


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateField()
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="homeTeam"
    )
    away_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="awayTeam"
    )


class PlayerStat(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    assists = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    shots = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sca = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    touches = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    passes = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    carries = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tackled = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    interceptions = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    blocks = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)


class PlayerStatSum(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    attack = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    defense = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)


class TeamStat(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    assists = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    shots = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sca = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tackled = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    interceptions = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    blocks = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)


class GameData(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game")
    home_team_players = models.ManyToManyField(Player, related_name="home_team_players")
    away_team_players = models.ManyToManyField(Player, related_name="away_team_players")
