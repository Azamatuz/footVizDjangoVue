from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Game, Team, Player, Stat, GameData
from .serializers import (
    GameSerializer,
    TeamSerializer,
    PlayerSerializer,
    StatSerializer,
)


class ListGame(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class DetailGame(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ListTeam(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class DetailTeam(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ListPlayer(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class DetailPlayer(RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class ListStat(ListAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer


class DetailStat(RetrieveAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer


class ListGameData(ListAPIView):
    queryset = GameData.objects.all()
    serializer_class = GameSerializer


class DetailGameData(RetrieveAPIView):
    queryset = GameData.objects.all()
    serializer_class = GameSerializer
