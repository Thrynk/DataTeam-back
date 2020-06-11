from rest_framework import serializers
from api import models as my_models

from django.shortcuts import render, redirect

import requests

# un Serializers sert à reprensenter la donnée en un format adapté à une API (Json).

class TennisPlayerListSerializer(serializers.ModelSerializer):
#class TennisPlayerSerializer(serializers.HyperlinkedModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api2:tennisPlayer-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.TennisPlayer
        fields = [
            'id',
            'name',
            'firstname',
            'nationality',
            'url_detail',
            ]

class TennisPlayerDetailSerializer(serializers.ModelSerializer):

    url_match = serializers.HyperlinkedIdentityField(
        view_name='api2:tennisPlayer-match',
        lookup_field='id'
        )

    url_stats = serializers.HyperlinkedIdentityField(
        view_name='api2:tennisPlayer-stats',
        lookup_field='id'
        )

    class Meta:
        model = my_models.TennisPlayer
        fields = [
            'id',
            'name',
            'firstname',
            'nationality',
            'url_match',
            'url_stats',
            ]

####################################################################################

class MatchListSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api2:match-detail',
        lookup_field='id'
        )

    winner_name=serializers.SerializerMethodField()
    winner_firstname=serializers.SerializerMethodField()
    loser_name=serializers.SerializerMethodField()
    loser_firstname=serializers.SerializerMethodField()
    tournament_event_name=serializers.SerializerMethodField()

    class Meta:
        model = my_models.Match
        fields=[
            'id',
            'winner',
            'winner_name',
            'winner_firstname',
            'loser',
            'loser_name',
            'loser_firstname',
            'tournament_event',
            'tournament_event_name',
            'score',
            'date',
            'round',
            'url_detail',
            ]

    def get_winner_name(self, obj):
        return str(obj.winner.name)

    def get_winner_firstname(self, obj):
        return str(obj.winner.firstname)

    def get_loser_name(self, obj):
        return str(obj.loser.name + " " + obj.loser.firstname)

    def get_loser_firstname(self, obj):
        return str(obj.winner.firstname)

    def get_tournament_event_name(self, obj):
        return str(obj.tournament_event.tournament.name)

class MatchDetailSerializer(serializers.ModelSerializer):

    url_stats = serializers.HyperlinkedIdentityField(
        view_name='api2:match-stats',
        lookup_field='id'
        )

    winner_name=serializers.SerializerMethodField()
    loser_name=serializers.SerializerMethodField()
    tournament_event_name=serializers.SerializerMethodField()

    all_match_winner = serializers.SerializerMethodField()
    all_match_loser = serializers.SerializerMethodField()

    class Meta:
        model = my_models.Match
        fields=[
            'id',
            'winner',
            'winner_name',
            'loser',
            'loser_name',
            'tournament_event',
            'tournament_event_name',
            'score',
            'date',
            'round',
            'url_stats',
            'all_match_winner',
            'all_match_loser'
            ]

    def get_winner_name(self, obj):
        return str(obj.winner.name + " " + obj.winner.firstname)

    def get_loser_name(self, obj):
        return str(obj.loser.name + " " + obj.loser.firstname)

    def get_tournament_event_name(self, obj):
        return str(obj.tournament_event.tournament.name)

    def get_all_match_winner(self, obj):
        url='http://192.168.43.51/api2/tennisPlayer/{id}/match/?page_nombre=all'.format(id=str(obj.winner.id))
        content = requests.get(url)
        data = content.json()
        return data["results"]

    def get_all_match_loser(self, obj):
        url='http://192.168.43.51/api2/tennisPlayer/{id}/match/?page_nombre=all'.format(id=str(obj.loser.id))
        content = requests.get(url)
        data = content.json()
        return data["results"]

####################################################################################

class MatchStatsListSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api2:matchStats-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.MatchStats
        fields=[
            'id',
            'match'
            'winner_ace',
            'winner_df',
            'winner_serve_points',
            'winner_1st_in',
            'winner_1st_won',
            'winner_2st_won',
            'loser_ace',
            'loser_df',
            'loser_serve_points',
            'loser_1st_in',
            'loser_1st_won',
            'loser_2st_won',
            'url_detail'
            ]

class MatchStatsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = my_models.MatchStats
        fields=[
            'id',
            'match'
            'winner_ace',
            'winner_df',
            'winner_serve_points',
            'winner_1st_in',
            'winner_1st_won',
            'winner_2st_won',
            'loser_ace',
            'loser_df',
            'loser_serve_points',
            'loser_1st_in',
            'loser_1st_won',
            'loser_2st_won',
            ]

####################################################################################

class TennisPlayerStatsListSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api2:tennisPlayerStats-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.TennisPlayerStats
        fields=[
            'id',
            'player',
            'matches_won',
            'matches_lost',
            'sets_won',
            'sets_lost',
            'aces',
            'double_faults',
            'serve_points',
            'first_in',
            'first_won',
            'second_won',
            'others_serve_points',
            'others_1st_in',
            'others_1st_won',
            'others_2nd_won',
            'others_breakpoints_saved',
            'others_breakpoints_faced',
            'url_detail'
            ]

class TennisPlayerStatsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = my_models.TennisPlayerStats
        fields=[
            'id',
            'player',
            'matches_won',
            'matches_lost',
            'sets_won',
            'sets_lost',
            'aces',
            'double_faults',
            'serve_points',
            'first_in',
            'first_won',
            'second_won',
            'others_serve_points',
            'others_1st_in',
            'others_1st_won',
            'others_2nd_won',
            'others_breakpoints_saved',
            'others_breakpoints_faced',
            ]

####################################################################################

class TournamentListSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api2:tournament-detail',
        lookup_field='id'
        ) 

    class Meta:
        model = my_models.Tournament
        fields=[
            'id',
            'name',
            'surface',
            'date',
            'city',
            'url_detail'
            ]

class TournamentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = my_models.Tournament
        fields=[
            'id',
            'name',
            'surface',
            'date',
            'city',
            ]

####################################################################################

class TournamentEventListSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api2:tournamentEvent-detail',
        lookup_field='id'
        )

    tournament_name=serializers.SerializerMethodField()

    class Meta:
        model = my_models.TournamentEvent
        fields=[
            'id',
            'tournament',
            'tournament_name',
            'season',
            'date',
            'url_detail',
            ]

    def get_tournament_name(self, obj):
        return str(obj.tournament.name)

class TournamentEventDetailSerializer(serializers.ModelSerializer):

    tournament_name=serializers.SerializerMethodField()

    class Meta:
        model = my_models.TournamentEvent
        fields=[
            'id',
            'tournament',
            'tournament_name',
            'season',
            'date'
            ]

    def get_tournament_name(self, obj):
        return str(obj.tournament.name)

####################################################################################

class AnecdoteListSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api2:anecdote-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.Anecdote
        fields=[
            'title',
            'url_detail'
            ]

class AnecdoteDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = my_models.Anecdote
        fields=[
            'id',
            'title',
            'content',
            ]

####################################################################################

