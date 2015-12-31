from data.models import Sport, League, Team, Position, Player, PlayerNews
from rest_framework.serializers import HyperlinkedModelSerializer


class SportSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Sport
        fields = ('name', 'abbreviation')


class LeagueSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = League
        fields = ('sport', 'name', 'abbreviation')


class PositionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('sport', 'name', 'abbreviation')


class TeamSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('league', 'name', 'abbreviation')


class PlayerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('team', 'position', 'first_name', 'last_name', 'rotoworld_url')


class PlayerNewsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PlayerNews
        fields = ('player', 'report', 'impact', 'timestamp')