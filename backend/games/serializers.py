from rest_framework import serializers
from .models import Game, Team, Player, Stat


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ("id", "assists", "goals", "passes", "blocks")


class PlayerSerializer(serializers.ModelSerializer):
    stats = StatSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ("id", "name", "number", "birthday", "stats")


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ("id", "name", "city", "division", "players")


class GameSerializer(serializers.ModelSerializer):
    home_team = TeamSerializer(read_only=True)
    home_team_players = PlayerSerializer(many=True, read_only=True)
    away_team = TeamSerializer(read_only=True)
    away_team_players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = (
            "id",
            "date",
            "home_team",
            "away_team",
            "home_team_players",
            "away_team_players",
        )


class GameDataSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    home_team_players = PlayerSerializer(many=True, read_only=True)
    away_team_players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ("id", "game", "home_team_players", "away_team_players")
