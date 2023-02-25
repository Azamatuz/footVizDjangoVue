from django.urls import path
from .views import (
    ListGame,
    DetailGame,
    ListTeam,
    DetailTeam,
    ListPlayer,
    DetailPlayer,
    ListStat,
    DetailStat,
    ListGameData,
    DetailGameData,
)

urlpatterns = [
    path("games/<int:pk>/", DetailGame.as_view()),
    path("games/", ListGame.as_view()),
    path("teams/<int:pk>/", DetailTeam.as_view()),
    path("teams/", ListTeam.as_view()),
    path("players/<int:pk>/", DetailPlayer.as_view()),
    path("players/", ListPlayer.as_view()),
    path("stats/<int:pk>/", DetailStat.as_view()),
    path("stats/", ListStat.as_view()),
    path("game-data/<int:pk>/", DetailGameData.as_view()),
    path("game-data/", ListGameData.as_view()),
]
