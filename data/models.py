from __future__ import unicode_literals

from django.db.models import Model, TextField, CharField, DateTimeField, URLField, ForeignKey, CASCADE


class Sport(Model):
    name = CharField(max_length=100)
    abbreviation = CharField(max_length=10)

    class Meta:
        unique_together = ('name', 'abbreviation')


class League(Model):
    sport = ForeignKey(Sport, on_delete=CASCADE)
    name = CharField(max_length=100)
    abbreviation = CharField(max_length=10)

    class Meta:
        unique_together = ('sport', 'name', 'abbreviation')


class Position(Model):
    sport = ForeignKey(Sport, on_delete=CASCADE)
    name = CharField(max_length=100)
    abbreviation = CharField(max_length=10)

    class Meta:
        unique_together = ('sport', 'name', 'abbreviation')


class Team(Model):
    league = ForeignKey(League, on_delete=CASCADE)
    name = CharField(max_length=100)
    abbreviation = CharField(max_length=10)

    class Meta:
        unique_together = ('league', 'name', 'abbreviation')


class Player(Model):
    team = ForeignKey(Team, on_delete=CASCADE)
    position = ForeignKey(Position, on_delete=CASCADE)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    rotoworld_url = URLField(null=True)

    class Meta:
        unique_together = ('team', 'position', 'first_name', 'last_name', 'rotoworld_url')


class PlayerNews(Model):
    player = ForeignKey(Player, on_delete=CASCADE)
    report = TextField()
    impact = TextField()
    timestamp = DateTimeField()

    class Meta:
        unique_together = ('player', 'report', 'impact', 'timestamp')
