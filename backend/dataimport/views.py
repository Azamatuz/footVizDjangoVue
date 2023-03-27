from pyexpat.errors import messages
from django.shortcuts import render, redirect
import csv
import io
from games.models import Stat, Player, Team, Game, GameData
from .forms import DataImportForm


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
            game, created = Game.objects.get_or_create(date=game_date, home_team=home_team, away_team=away_team)
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
                    "passes": row["Pass"],
                    "carries": row["Carries"],
                    "tackled": row["Tackled"],
                    "interceptions": row["Interceptions"],
                    "blocks": row["Blocks"],
                }
                home_performance, created = Stat.objects.get_or_create(**home_data)
                # player can have multiple stats for different games
                home_player, created = Player.objects.get_or_create(name=row[""])
                home_player.stats.add(home_performance)
                # add player to home team
                home_team.players.add(home_player)

            away_team_csv = request.FILES["away_team_csv"]
            away_decoded_file = away_team_csv.read().decode("utf-8").splitlines()

            away_reader = csv.DictReader(away_decoded_file)
            for row in away_reader:
                # create player performance
                away_data = {
                    "shots": row["Shots"],
                    "sca": row["SCA"],
                    "touches": row["Touches"],
                    "passes": row["Pass"],
                    "carries": row["Carries"],
                    "tackled": row["Tackled"],
                    "interceptions": row["Interceptions"],
                    "blocks": row["Blocks"],
                }
                away_performance, created = Stat.objects.get_or_create(**away_data)
                # player can have multiple stats for different games
                away_player, created = Player.objects.get_or_create(name=row[""])
                away_player.stats.add(away_performance)
                # add player to home team
                away_team.players.add(away_player)


            # messages.success(request, 'Data imported successfully')
            return redirect("data_imported")
    else:
        form = DataImportForm()

    context = {"form": form}
    return render(request, "import.html", context)


def data_imported(request):
    return render(request, "data_imported.html")
