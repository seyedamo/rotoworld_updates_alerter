import csv
import os
from datetime import datetime

from lxml import html
from pytz import utc, timezone
from selenium import webdriver

from data.inserters.utils import rotoworld_team_nickname_to_abbreviation, doneTextSend
from data.models import Sport, League, Position, Team, Player, PlayerNews


def insert_sports():
    sports = [
        {
            'name': 'BASKETBALL',
            'abbreviation': 'BBALL'
        }
    ]
    for sport in sports:
        Sport.objects.get_or_create(name=sport['name'], abbreviation=sport['abbreviation'])


def insert_leagues():
    leagues = [
        {
            'sport_name': 'BASKETBALL',
            'name': 'NATIONAL BASKETBALL ASSOCIATION',
            'abbreviation': 'NBA'
        }
    ]
    for league in leagues:
        sport = Sport.objects.get(name=league['sport_name'])
        League.objects.get_or_create(sport=sport, name=league['name'], abbreviation=league['abbreviation'])


def insert_positions():
    positions = [
        {
            'sport_name': 'BASKETBALL',
            'name': 'GUARD',
            'abbreviation': 'G'
        },
        {
            'sport_name': 'BASKETBALL',
            'name': 'FORWARD',
            'abbreviation': 'F'
        },
        {
            'sport_name': 'BASKETBALL',
            'name': 'CENTER',
            'abbreviation': 'C'
        },
        {
            'sport_name': 'BASKETBALL',
            'name': 'GUARD/FORWARD',
            'abbreviation': 'G/F'
        },
        {
            'sport_name': 'BASKETBALL',
            'name': 'FORWARD/CENTER',
            'abbreviation': 'F/C'
        }
    ]
    for position in positions:
        sport = Sport.objects.get(name=position['sport_name'])
        Position.objects.get_or_create(sport=sport, name=position['name'], abbreviation=position['abbreviation'])


def insert_nba_teams(team_name_csv):
    with open(team_name_csv) as file:
        reader = csv.reader(file)
        nba_team_name_list = list(reader)[1:]
        for team in nba_team_name_list:
            league = League.objects.get(abbreviation=team[0])
            Team.objects.get_or_create(league=league, name=team[2], abbreviation=team[1])


def insert_teams(nba_team_name_csv):
    insert_nba_teams(nba_team_name_csv)


def insert_player_news_source(source):
    all_new_player_news = False
    tree = html.fromstring(source)
    raw_players = tree.xpath("//div[@class='player']/a/text()")
    raw_player_links = tree.xpath("//div[@class='player']/a/@href")
    raw_player_positions = tree.xpath("//div[@class='player']/text()")
    players = list()
    for counter in range(0, len(raw_players)):
        if counter % 2 == 0:
            players.append([raw_players[counter], raw_players[counter + 1], raw_player_links[counter], raw_player_positions[counter].encode('utf-8').replace("-", "").replace("\n", "").strip()])
    player_reports = tree.xpath("//div[@class='report']/p/text()")
    player_impacts = tree.xpath("//div[@class='impact']/text()")[3:]
    raw_datetime = tree.xpath("//div[@class='info']/div[@class='date']/text()")
    for index in range(0, len(players)):
        players_data = players[index]
        players_data.append(player_reports[index].encode('utf-8').replace("\n", "").strip())
        players_data.append(player_impacts[index].encode('utf-8').replace("\n", "").strip())
        # players_data.append(timezone("US/Eastern").localize(datetime.strptime("{0} {1}".format(datetime.now(timezone("US/Eastern")).year, raw_datetime[index]), "%Y %b %d - %I:%M %p")).astimezone(utc))
        players[index] = players_data
    for player in players:
        team = Team.objects.get(abbreviation=rotoworld_team_nickname_to_abbreviation(player[1]))
        position = Position.objects.get(abbreviation=player[3])
        player_names = player[0].split(" ")
        player_obj, created = Player.objects.get_or_create(team=team, position=position, first_name=player_names[0], last_name=player_names[1], rotoworld_url=player[2])
        playerNews, created = PlayerNews.objects.get_or_create(player=player_obj, report=player[4], impact=player[5])
        if created:
            doneTextSend(
                    "Rotoworld Update for {0} {1}".format(playerNews.player.first_name, playerNews.player.last_name),
                    playerNews.report,
                    playerNews.impact
            )
            all_new_player_news = True
    return all_new_player_news


def insert_player_news(chromedriver_path):
    os.environ["webdriver.chrome.driver"] = chromedriver_path
    rotoworld_player_url = "http://www.rotoworld.com/playernews/nba/basketball-player-news"
    driver = webdriver.PhantomJS(executable_path=chromedriver_path)
    try:
        driver.get(rotoworld_player_url)
        source = driver.page_source
        while insert_player_news_source(source):
            driver.find_element_by_name("ctl00$cp1$ctl00$btnNavigate1").click()
            source = driver.page_source
    finally:
        driver.close()
