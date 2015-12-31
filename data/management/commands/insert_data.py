from django.core.management.base import BaseCommand

from data.inserters.inserters import insert_sports, insert_leagues, insert_positions, insert_teams, insert_player_news


class Command(BaseCommand):
    def handle(self, *args, **options):
        insert_sports()
        insert_leagues()
        insert_positions()
        insert_teams(nba_team_name_csv='data/inserters/static/nba_team_name_mapping.csv')
        insert_player_news('/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')