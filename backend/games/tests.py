from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Game


class GameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Game.objects.create(date="2023-01-01", home_team="Juventus", away_team="Torino")

    def test_game_date(self):
        game = Game.objects.get(id=1)
        expected_object_name = f"{game.date}"
        self.assertEqual(expected_object_name, "2023-01-01")

    def test_game_home_team(self):
        game = Game.objects.get(id=1)
        expected_object_name = f"{game.home_team}"
        self.assertEqual(expected_object_name, "Juventus")
