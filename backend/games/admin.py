from django.contrib import admin
from .models import Game, Team, Player, Stat, GameData

# Register your models here.
admin.site.register(Game)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Stat)
admin.site.register(GameData)

