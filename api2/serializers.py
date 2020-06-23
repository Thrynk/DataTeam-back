from rest_framework import serializers
from rest_framework.reverse import reverse

from django.shortcuts import render, redirect

from api2 import models as my_models

import requests

# un Serializers sert à reprensenter la donnée queryset type de django en un format adapté à une API (ici Json).

####################################################################################

class HyperlinkedIdentityFieldWithLookup_fields(serializers.HyperlinkedIdentityField):

    lookup_fields = [
        ]

    def getattrList(self,List):
        for i in range (0,len(List)-1):
            a=getattr(List[i],List[i+1])
            print(a)
        return a

    def __init__(self, *args, **kwargs):
        self.lookup_fields = kwargs.pop('lookup_fields', self.lookup_fields)
        super().__init__(*args, **kwargs)

    def get_url(self, obj, view_name, request, format):
        kwargs = {}
        for url_param, model_field in self.lookup_fields:
            attr = obj
            for field in model_field.split('.'):
                attr = getattr(attr,field)
            kwargs[url_param] = attr

        return reverse(view_name, kwargs=kwargs, request=request, format=format)

####################################################################################

class TennisPlayerListSerializer(serializers.ModelSerializer):

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

    url_stats_return = serializers.HyperlinkedIdentityField(
        view_name='api2:tennisPlayer-returnstats',
        lookup_field='id'
        )

    url_flag = serializers.HyperlinkedIdentityField(
        view_name='api2:tennisPlayer-flag',
        lookup_field='id',
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
            'url_stats_return',
            'url_flag',
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

    url_winner_flag = HyperlinkedIdentityFieldWithLookup_fields(
        view_name='api2:tennisPlayer-flag',
        lookup_fields=[('id', 'winner.id'),
                       ],
        )

    url_loser_flag = HyperlinkedIdentityFieldWithLookup_fields(
        view_name='api2:tennisPlayer-flag',
        lookup_fields=[('id', 'loser.id'),
                        ],
        )

    class Meta:
        model = my_models.Match
        fields=[
            'id',
            'winner',
            'winner_name',
            'winner_firstname',
            'url_winner_flag',
            'loser',
            'loser_name',
            'loser_firstname',
            'url_loser_flag',
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
        return str(obj.loser.name)

    def get_loser_firstname(self, obj):
        return str(obj.loser.firstname)

    def get_tournament_event_name(self, obj):
        return str(obj.tournament_event.tournament.name)

class MatchDetailSerializer(serializers.ModelSerializer):

    url_stats = serializers.HyperlinkedIdentityField(
        view_name='api2:match-stats',
        lookup_field='id'
        )

    url_predictions = serializers.HyperlinkedIdentityField(
        view_name='api2:match-predictions',
        lookup_field='id'
        )

    winner_name=serializers.SerializerMethodField()
    winner_firstname=serializers.SerializerMethodField()
    loser_name=serializers.SerializerMethodField()
    loser_firstname=serializers.SerializerMethodField()
    tournament_event_name=serializers.SerializerMethodField()

    all_match_winner = serializers.SerializerMethodField()
    all_match_loser = serializers.SerializerMethodField()

    url_winner_flag = HyperlinkedIdentityFieldWithLookup_fields(
        view_name='api2:tennisPlayer-flag',
        lookup_fields=[('id', 'winner.id'),
                       ],
        )

    url_loser_flag = HyperlinkedIdentityFieldWithLookup_fields(
        view_name='api2:tennisPlayer-flag',
        lookup_fields=[('id', 'loser.id'),
                        ],
        )

    url_tennisplayersstats = HyperlinkedIdentityFieldWithLookup_fields(
        view_name='api2:match-tennisplayersstats',
        lookup_fields=[('id', 'id'),
                        ],
        )

    url_tennisplayersstatsreturn = HyperlinkedIdentityFieldWithLookup_fields(
        view_name='api2:match-tennisplayersstatsreturn',
        lookup_fields=[('id', 'id'),
                        ],
        )
    

    class Meta:
        model = my_models.Match
        fields=[
            'id',
            'winner',
            'winner_name',
            'winner_firstname',
            'url_winner_flag',
            'loser',
            'loser_name',
            'loser_firstname',
            'url_loser_flag',
            'tournament_event',
            'tournament_event_name',
            'score',
            'date',
            'round',
            'url_stats',
            'url_predictions',
            "url_tennisplayersstats",
            "url_tennisplayersstatsreturn",
            'all_match_winner',
            'all_match_loser',
            ]

    def get_winner_name(self, obj):
        return str(obj.winner.name)

    def get_winner_firstname(self, obj):
        return str(obj.winner.firstname)

    def get_loser_name(self, obj):
        return str(obj.loser.name)

    def get_loser_firstname(self, obj):
        return str(obj.loser.firstname)

    def get_tournament_event_name(self, obj):
        return str(obj.tournament_event.tournament.name)

    def get_all_match_winner(self, obj):
        request = self.context['request']
        url=request.build_absolute_uri('/api2/tennisPlayer/{id}/match/?page_nombre=100&orderby=-date&date__lte={date}'.format(id=str(obj.winner.id),date=str(obj.date)))
        content = requests.get(url)
        data = content.json()
        return data["results"]

    def get_all_match_loser(self, obj):
        request = self.context['request']
        url=request.build_absolute_uri('/api2/tennisPlayer/{id}/match/?page_nombre=100&orderby=-date&date__lte={date}'.format(id=str(obj.loser.id),date=str(obj.date)))
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
            'match',
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
            'player_id',
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

class Player_StatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = my_models.Player_stats
        fields=[
            'ace',
            'df',
            'serve_points',
            'first_in',
            'first_won',
            'second_won',
            'first_serve_success_percentage',
            'first_serve_won_percentage',
            'second_serve_won_percentage',
            'ace_percentage',
            'df_percentage',
            'firstname',
            'name',
            'player_id',
            ]

class Player_Stats_ReturnSerializer(serializers.ModelSerializer):

    class Meta:
        model = my_models.Player_stats_return
        fields=[
            'opponent_ace',
            'opponent_df',
            'opponent_serve_points',
            'opponent_first_in',
            'opponent_first_won',
            'opponent_second_won',
            'winning_on_return_percentage',
            'winning_on_1st_serve_return_percentage',
            'winning_on_2nd_serve_return_percentage',
            'firstname',
            'name',
            'player_id',
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

    #url_detail = serializers.HyperlinkedIdentityField(
    #    view_name='api2:anecdote-detail',
    #    lookup_field='id'
    #    )

    class Meta:
        model = my_models.Anecdote
        fields=[
            'id',
            'title',
            'content',
            #'url_detail'
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

class MeteoListSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api2:meteo-detail',
        lookup_field='id'
        )

    url_meteo_image = HyperlinkedIdentityFieldWithLookup_fields(
        view_name='api2:meteo-image',
        lookup_fields=[('id', 'id'),
                        ],
        )

    class Meta:
        model = my_models.Meteo
        fields = [
            'id',
            'location_latitude',
            'location_longitude',
            'temperature',
            'humidity',
            'precipitation',
            'date_time',
            'url_detail',
            'url_meteo_image',
            ]

class MeteoDetailSerializer(serializers.ModelSerializer):

    url_meteo_image = HyperlinkedIdentityFieldWithLookup_fields(
        view_name='api2:meteo-image',
        lookup_fields=[('id', 'id'),
                        ],
        )

    class Meta:
        model = my_models.Meteo
        fields = [
            'id',
            'location_latitude',
            'location_longitude',
            'temperature',
            'humidity',
            'precipitation',
            'date_time',
            'url_meteo_image',
            ]

####################################################################################

class CityListSerializer(serializers.ModelSerializer):
#class TennisPlayerSerializer(serializers.HyperlinkedModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api2:city-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.City
        fields = [
            'id',
            'name',
            'location_latitude',
            'location_longitude',
            'last_load',
            'url_detail',
            ]

####################################################################################

class PredictionSerializer(serializers.ModelSerializer):

    player1_name = serializers.SerializerMethodField()
    player2_name = serializers.SerializerMethodField()

    winner = serializers.SerializerMethodField()

    class Meta:
        model = my_models.Prediction
        fields = [
            'id',
            'match',
            'player1',
            'player1_name',
            'player1_proba',
            'player2',
            'player2_name',
            'player2_proba',
            'winner',
            ]

    def get_player1_name(self, obj):
        return obj.player1.name + " " + obj.player1.firstname
        return my_models.TennisPlayer.objects.get(id=obj.player1.id).name + " " + my_models.TennisPlayer.objects.get(id=obj.player1.id).firstname

    def get_player2_name(self, obj):
        return obj.player2.name + " " + obj.player2.firstname
        return my_models.TennisPlayer.objects.get(id=obj.player2.id).name + " " + my_models.TennisPlayer.objects.get(id=obj.player2.id).firstname

    def get_winner(seld, obj):
        return obj.match.winner.id