from pyexpat.errors import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import csv
import io
from games.models import Game, Team, Player, PlayerStat, PlayerStatSum, TeamStat
from .forms import DataImportForm, PlayerImportForm


@login_required
def import_data(request):
    if request.method == "POST":
        form = DataImportForm(request.POST, request.FILES)
        if form.is_valid():
            # save game date game_date
            game_date = form.cleaned_data["game_date"]

            # save home team
            home_team_name = form.cleaned_data["home_team_name"]
            home_team, created = Team.objects.get_or_create(name=home_team_name)

            away_team_name = form.cleaned_data["away_team_name"]
            away_team, created = Team.objects.get_or_create(name=away_team_name)

            # create game
            game, created = Game.objects.get_or_create(
                date=game_date, home_team=home_team, away_team=away_team
            )

            # process the uploaded file
            home_team_csv = request.FILES["home_team_csv"]
            home_decoded_file = home_team_csv.read().decode("utf-8").splitlines()

            home_reader = csv.DictReader(home_decoded_file)
            for row in home_reader:
                # create player performance
                home_data = {
                    "shots": row["Shots"],
                    "sca": row["SCA"],
                    "touches": row["Touches"],
                    "passes": row["Passes"],
                    "carries": row["Carries"],
                    "tackled": row["Tackled"],
                    "interceptions": row["Interceptions"],
                    "blocks": row["Blocks"],
                }
                home_data_sum = {"attack": row["Attack"], "defense": row["Defense"]}
                home_player, created = Player.objects.get_or_create(name=row[""], team=home_team)
                home_performance, created = PlayerStat.objects.get_or_create(
                    game=game, player=home_player, defaults=home_data
                )
                home_performance_sum, created = PlayerStatSum.objects.get_or_create(
                    game=game, player=home_player, defaults=home_data_sum)

            away_team_csv = request.FILES["away_team_csv"]
            away_decoded_file = away_team_csv.read().decode("utf-8").splitlines()

            away_reader = csv.DictReader(away_decoded_file)
            for row in away_reader:
                # create player performance
                away_data = {
                    "shots": row["Shots"],
                    "sca": row["SCA"],
                    "touches": row["Touches"],
                    "passes": row["Passes"],
                    "carries": row["Carries"],
                    "tackled": row["Tackled"],
                    "interceptions": row["Interceptions"],
                    "blocks": row["Blocks"],
                }
                away_data_sum = {"attack": row["Attack"], "defense": row["Defense"]}

                away_player, created = Player.objects.get_or_create(name=row[""], team=away_team)
                away_performance, created = PlayerStat.objects.get_or_create(
                    game=game, player=away_player, defaults=away_data)
                away_performance_sum, created = PlayerStatSum.objects.get_or_create(
                    game=game, player=away_player, defaults=away_data_sum)
            # messages.success(request, 'Data imported successfully')
            return redirect("data_imported")
    else:
        form = DataImportForm()

    context = {"form": form}
    return render(request, "import-game.html", context)

@login_required
def import_players(request):
    if request.method == "POST":
        form = PlayerImportForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.cleaned_data["team"]
            team, created = Team.objects.get_or_create(name=team)
            # process the uploaded file
            player_csv= request.FILES["player_csv"]
            player_decoded_file = player_csv.read().decode("utf-8").splitlines()

            player_reader = csv.DictReader(player_decoded_file)
            for row in player_reader:
                player = Player.objects.create(name=row["Player"], team=team)
            return redirect("import_game_data")
    else:
        form = PlayerImportForm()

    context = {"form": form}
    return render(request, "import-players.html", context)


def data_imported(request):
    return render(request, "data_imported.html")
