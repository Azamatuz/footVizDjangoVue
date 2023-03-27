from django import forms

class DataImportForm(forms.Form):
    game_date = forms.DateField()
    home_team_name = forms.CharField()
    away_team_name = forms.CharField()
    home_team_csv = forms.FileField()
    away_team_csv = forms.FileField()