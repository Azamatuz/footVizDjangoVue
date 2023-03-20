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
            # process the uploaded file
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode("utf-8").splitlines()

            reader = csv.DictReader(decoded_file)
            for row in reader:
                # create player performance
                data = {
                    "shots": row["Shots"],
                    "sca": row["SCA"],
                    "touches": row["Touches"],
                    "passes": row["Passes"],
                    "carries": row["Carries"],
                    "press": row["Press"],
                    "tackled": row["Tackled"],
                    "interceptions": row["Interceptions"],
                    "blocks": row["Blocks"],
                }
                performance, created = Stat.objects.get_or_create(**data)
                # player can have multiple stats for different games
                player, created = Player.objects.get_or_create(name=row['Player'])
                player.stats.set(performance)



            # messages.success(request, 'Data imported successfully')
            return redirect("data_imported")
    else:
        form = DataImportForm()

    context = {"form": form}
    return render(request, "import.html", context)


def data_imported(request):
    return render(request, "data_imported.html")
