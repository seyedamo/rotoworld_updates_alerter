from django.core.management.base import BaseCommand

from data.inserters.inserters import insert_sports, insert_leagues, insert_positions, insert_teams, insert_player_news
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '../../../chromedriver')
        insert_sports()
        insert_leagues()
        insert_positions()
        insert_teams(nba_team_name_csv='data/inserters/static/nba_team_name_mapping.csv')
        insert_player_news(filename)