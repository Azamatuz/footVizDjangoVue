from django import forms

class DataImportForm(forms.Form):
    game_date = forms.DateField()
    team = forms.CharField()
    #away_team = forms.CharField()
    csv_file = forms.FileField()