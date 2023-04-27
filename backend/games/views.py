from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Game, GameData, Team, Player, PlayerStat, PlayerStatSum, TeamStat
from .serializers import (
    GameSerializer,
    TeamSerializer,
    TeamStatSerializer,
    PlayerSerializer,
    PlayerStatSerializer,
    PlayerStatSumSerializer,
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

class ListTeamStat(ListAPIView):
    queryset = TeamStat.objects.all()
    serializer_class = TeamStatSerializer


class DetailTeamStat(RetrieveAPIView):
    queryset = TeamStat.objects.all()
    serializer_class = TeamStatSerializer


class ListPlayer(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class DetailPlayer(RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class ListStat(ListAPIView):
    queryset = PlayerStat.objects.all()
    serializer_class = PlayerStatSerializer


class DetailStat(RetrieveAPIView):
    queryset = PlayerStat.objects.all()
    serializer_class = PlayerStatSerializer


class ListPlayerStat(ListAPIView):
    queryset = PlayerStat.objects.all()
    serializer_class = PlayerStatSerializer


class DetailPlayerStat(RetrieveAPIView):
    queryset = PlayerStat.objects.all()
    serializer_class = PlayerStatSerializer


class ListPlayerStatSum(ListAPIView):
    queryset = PlayerStatSum.objects.all()
    serializer_class = PlayerStatSumSerializer


class DetailPlayerStatSum(RetrieveAPIView):
    queryset = PlayerStatSum.objects.all()
    serializer_class = PlayerStatSumSerializer


class GameStatView(ListAPIView):
    serializer_class = PlayerStatSerializer

    def get_queryset(self):
        game_id = self.kwargs.get('game_id', None)
        queryset = PlayerStat.objects.all()
        queryset = queryset.filter(game_id=game_id)
        return queryset


class PlayerStatSumView(ListAPIView):
    serializer_class = PlayerStatSumSerializer

    def get_queryset(self):
        game_id = self.kwargs.get('game_id', None)
        queryset = PlayerStatSum.objects.all()
        if game_id is not None:
            queryset = queryset.filter(game_id=game_id)
        return queryset
