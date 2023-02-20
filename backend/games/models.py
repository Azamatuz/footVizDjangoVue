from django.db import models

# Create your models here.
class Game(models.Model):
    date = models.DateField()
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)

    def __str__(self):
        return self.date
