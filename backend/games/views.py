from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Game
from .serializers import GameSerializer


class ListGame(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class DetailGame(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer