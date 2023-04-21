from rest_framework import serializers
from .models import Team, Player, Game, PlayerStat, PlayerStatSum, TeamStat


class PlayerStatSerializer(serializers.ModelSerializer):
    player_name = serializers.CharField(source='player.name')
    player_team = serializers.CharField(source='player.team')
    class Meta:
        model = PlayerStat
        fields = ['player_name', 'player_team', 'shots', 'sca', 'tackled', 'interceptions', 'blocks', 'touches', 'passes', 'carries']


class PlayerStatSumSerializer(serializers.ModelSerializer):
    player_name = serializers.CharField(source='player.name')
    player_team = serializers.CharField(source='player.team')
    class Meta:
        model = PlayerStatSum
        fields = ['player_name', 'player_team', 'attack', 'defense']


class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()

    class Meta:
        model = Player
        fields = []


class TeamStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamStat
        fields = ['assists', 'shots', 'sca', 'tackled', 'interceptions', 'blocks']


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    home_team = serializers.StringRelatedField()
    away_team = serializers.StringRelatedField()

    class Meta:
        model = Game
        fields = ['id', 'date', 'home_team', 'away_team']
