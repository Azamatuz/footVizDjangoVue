from django.urls import path
from .views import (
    ListGame,
    DetailGame,
    ListTeam,
    DetailTeam,
    ListTeamStat,
    DetailTeamStat,
    ListPlayer,
    DetailPlayer,
    ListStat,
    DetailStat,
    ListPlayerStatSum,
    DetailPlayerStatSum,
    GameStatView,
    PlayerStatSumView,
)

urlpatterns = [
    path("games/", ListGame.as_view()),
    path("games/<int:pk>/", DetailGame.as_view()),
    path("teams/", ListTeam.as_view()),
    path("teams/<int:pk>/", DetailTeam.as_view()),
    path("team-stats/", ListTeamStat.as_view()),
    path("team-stats/<int:pk>/", DetailTeamStat.as_view()),
    path("players/", ListPlayer.as_view()),
    path("players/<int:pk>/", DetailPlayer.as_view()),
    path("stats/", ListStat.as_view()),
    path("stats/<int:pk>/", DetailStat.as_view()),
    path("player-stat-sum/", ListPlayerStatSum.as_view()),
    path("player-stat-sum/<int:pk>/", DetailPlayerStatSum.as_view()),
    path('game-stats/game=<int:game_id>/', GameStatView.as_view(), name='game-stats'),
    path('player-stats-sum/game=<int:game_id>/', PlayerStatSumView.as_view(), name='player-stats-sum'),
]
