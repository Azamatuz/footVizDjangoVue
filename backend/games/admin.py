from django.contrib import admin
from .models import Game, GameData, Team, Player, PlayerStat, PlayerStatSum, TeamStat

# Register your models here.
admin.site.register(Game)
admin.site.register(GameData)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(PlayerStat)
admin.site.register(PlayerStatSum)
admin.site.register(TeamStat)

