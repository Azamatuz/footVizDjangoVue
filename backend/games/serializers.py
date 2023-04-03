from rest_framework import serializers
from .models import Game, Team, Player, Stat, TeamStats


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        # all fields
        fields = "shots", "sca", "touches", "passes", "carries", "tackled", "interceptions", "blocks"


class PlayerSerializer(serializers.ModelSerializer):
    stats = StatSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ("name", "stats")


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ("name", "players")


class TeamStatsSerializer(serializers.ModelSerializer):
    stats = StatSerializer(many=True, read_only=True)

    class Meta:
        model = TeamStats
        fields = ("id", "stats")

class GameSerializer(serializers.ModelSerializer):
    teams_stats = TeamStatsSerializer(read_only=True)
    home_team = TeamSerializer(read_only=True)
    home_team_players = PlayerSerializer(read_only=True)
    away_team = TeamSerializer(read_only=True)
    away_team_players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = (
            "id",
            "date",
            "teams_stats",
            "home_team",
            "home_team_players",
            "away_team",
            "away_team_players",
        )


class GameDataSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    home_team_players = PlayerSerializer(many=True, read_only=True)
    away_team_players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ("id", "game", "home_team_players", "away_team_players")
