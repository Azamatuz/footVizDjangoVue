from django import forms
from django.urls import reverse_lazy
from games.models import Team

class DataImportForm(forms.Form):
    game_date = forms.DateField()
    home_team_name = forms.ChoiceField(choices=[])
    away_team_name = forms.ChoiceField(choices=[])
    home_team_csv = forms.FileField()
    away_team_csv = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(DataImportForm, self).__init__(*args, **kwargs)
        self.fields['home_team_name'].choices = self.get_team_choices()
        self.fields['away_team_name'].choices = self.get_team_choices()

    def get_team_choices(self):
        teams = Team.objects.all()
        choices = [('', 'Select a team')]
        choices += [(team.name, team.name) for team in teams]
        return choices

    def get_add_team_url(self):
        return reverse_lazy('import_players')


class PlayerImportForm(forms.Form):
    team = forms.CharField(label='Team Name', max_length=100)
    player_csv = forms.FileField(label='Player CSV')