from datetime import datetime

from pytz import utc
from rest_framework.viewsets import ReadOnlyModelViewSet

from data.models import Sport, League, Team, Position, Player, PlayerNews
from data.serializers import SportSerializer, LeagueSerializer, TeamSerializer, PositionSerializer, PlayerSerializer, PlayerNewsSerializer


# Create your views here.


class SportViewSet(ReadOnlyModelViewSet):
    serializer_class = SportSerializer

    def get_queryset(self):
        queryset = Sport.objects.all().order_by('name')
        name = self.request.query_params.get('name', None)
        abbreviation = self.request.query_params.get('abbreviation', None)
        if name is not None:
            queryset = queryset.filter(name=name)

        if abbreviation is not None:
            queryset = queryset.filter(abbreviation=abbreviation)

        return queryset


class LeagueViewSet(ReadOnlyModelViewSet):
    serializer_class = LeagueSerializer

    def get_queryset(self):
        queryset = League.objects.all().order_by('name')
        sport_abbreviation = self.request.query_params.get('sport_abbreviation', None)
        abbreviation = self.request.query_params.get('abbreviation', None)
        if sport_abbreviation is not None:
            queryset = queryset.filter(sport__abbreviation=sport_abbreviation)

        if abbreviation is not None:
            queryset = queryset.filter(abbreviation=abbreviation)

        return queryset


class TeamViewSet(ReadOnlyModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        queryset = Team.objects.all().order_by('name')
        abbreviation = self.request.query_params.get('abbreviation', None)
        league_abbreviation = self.request.query_params.get('league_abbreviation', None)

        if abbreviation is not None:
            queryset = queryset.filter(abbreviation=abbreviation)

        if league_abbreviation is not None:
            queryset = queryset.filter(league__abbreviation=league_abbreviation)

        return queryset


class PositionViewSet(ReadOnlyModelViewSet):
    serializer_class = PositionSerializer

    def get_queryset(self):
        queryset = Position.objects.all().order_by('name')
        abbreviation = self.request.query_params.get('abbreviation', None)
        sport_abbreviation = self.request.query_params.get('sport_abbreviation', None)
        if abbreviation is not None:
            queryset = queryset.filter(abbreviation=abbreviation)

        if sport_abbreviation is not None:
            queryset = queryset.filter(sport__abbreviation=sport_abbreviation)

        return queryset


class PlayerViewSet(ReadOnlyModelViewSet):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        queryset = Player.objects.all().order_by('first_name').order_by('last_name')
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)
        team_abbreviation = self.request.query_params.get('team_abbreviation', None)
        position_abbreviation = self.request.query_params.get('position_abbreviation', None)
        if first_name is not None:
            queryset = queryset.filter(first_name=first_name)

        if last_name is not None:
            queryset = queryset.filter(last_name=last_name)

        if team_abbreviation is not None:
            queryset = queryset.filter(team__abbreviation=team_abbreviation)

        if position_abbreviation is not None:
            queryset = queryset.filter(position__abbreviation=position_abbreviation)

        return queryset


class PlayerNewsViewSet(ReadOnlyModelViewSet):
    serializer_class = PlayerNewsSerializer

    def get_queryset(self):
        queryset = PlayerNews.objects.all().order_by('-id').order_by('-player__last_name').order_by('-player__first_name')
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)
        team_abbreviation = self.request.query_params.get('team_abbreviation', None)
        unix_start_time = self.request.query_params.get('unix_start_time', None)
        unix_end_time = self.request.query_params.get('unix_end_time', None)

        if first_name is not None:
            queryset = queryset.filter(player__first_name=first_name)

        if last_name is not None:
            queryset = queryset.filter(player__last_name=last_name)

        if team_abbreviation is not None:
            queryset = queryset.filter(team__abbreviation=team_abbreviation)

        if unix_start_time is not None:
            queryset = queryset.filter(timestamp__gte=datetime.fromtimestamp(unix_start_time, utc))

        if unix_end_time is not None:
            queryset = queryset.filter(timestamp__lte=datetime.fromtimestamp(unix_end_time, utc))

        return queryset
