from rest_framework import serializers
from . import models as my_models

from django.shortcuts import render, redirect



# un Serializers sert à reprensenter la donnée en un format adapté à une API (Json).


class TennisPlayerSerializer(serializers.ModelSerializer):
#class TennisPlayerSerializer(serializers.HyperlinkedModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:tennisPlayer-detail',
        lookup_field='id'
        )

    url_match = serializers.HyperlinkedIdentityField(
        view_name='api:tennisPlayer-match',
        lookup_field='id'
        )

    url_stats = serializers.HyperlinkedIdentityField(
        view_name='api:tennisPlayer-stats',
        lookup_field='id'
        )

    class Meta:
        model = my_models.TennisPlayer
        #fields = ['name','firstname','nationality','url_detail']
        #exclude = ['id']
        fields='__all__'


class MatchSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:match-detail',
        lookup_field='id'
        )

    url_stats = serializers.HyperlinkedIdentityField(
        view_name='api:match-stats',
        lookup_field='id'
        )

    #winner_name = serializers.CharField(default=my_models.TennisPlayer.objects.get(id=int(repr(my_models.Match.winner))))

    winner_name=serializers.SerializerMethodField()
    winner_firstname=serializers.SerializerMethodField()
    loser_name=serializers.SerializerMethodField()
    loser_firstname=serializers.SerializerMethodField()

    tournament_event_name=serializers.SerializerMethodField()

    class Meta:
        model = my_models.Match
        #exclude = ['id']
        fields='__all__'


    def get_winner_name(self, obj):
        return str(obj.winner.name)

    def get_winner_firstname(self, obj):
        return str(obj.winner.firstname)

    def get_loser_name(self, obj):
        return str(obj.loser.name + " " + obj.loser.firstname)

    def get_loser_firstname(self, obj):
        return str(obj.loser.firstname)

    def get_tournament_event_name(self, obj):
        return str(obj.tournament_event.tournament.name)

class MatchStatsSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:matchStats-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.MatchStats
        ##exclude = ['id']
        fields='__all__'

class TennisPlayerStatsSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:tennisPlayerStats-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.TennisPlayerStats
        #exclude = ['id']
        fields='__all__'

class TournamentSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:tournament-detail',
        lookup_field='id'
        ) 

    class Meta:
        model = my_models.Tournament
        #exclude = ['id']
        fields='__all__'


class TournamentEventSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:tournamentEvent-detail',
        lookup_field='id'
        )

    tournament_name=serializers.SerializerMethodField()

    class Meta:
        model = my_models.TournamentEvent
        #exclude = ['id']
        fields='__all__'


    def get_loser_name(self, obj):
        return str(obj.tournament.name)

    def get_tournament_name(self, obj):
        return str(obj.tournament.name)

class AnecdoteSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:anecdote-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.Anecdote
        #exclude = ['id']
        fields='__all__'

