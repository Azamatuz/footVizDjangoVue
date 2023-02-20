from django.urls import path
from .views import ListGame, DetailGame

urlpatterns = [
    path("games/<int:pk>/", DetailGame.as_view()),
    path("games/", ListGame.as_view()),
]
