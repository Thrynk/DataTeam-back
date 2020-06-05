from rest_framework import serializers
from . import models as my_models


# un Serializers sert à reprensenter la donnée en un format adapté à une API (Json).


class TennisPlayerSerializer(serializers.ModelSerializer):
#class TennisPlayerSerializer(serializers.HyperlinkedModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:tennisPlayer-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.TennisPlayer
        #fields = ['name','firstname','nationality','url_detail']
        exclude = ['id']

class MatchSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:match-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.Match
        exclude = ['id']

class MatchStatsSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:matchStats-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.MatchStats
        exclude = ['id']

class TennisPlayerStatsSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:tennisPlayerStats-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.TennisPlayerStats
        exclude = ['id']

class TournamentSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:tournament-detail',
        lookup_field='id'
        ) 

    class Meta:
        model = my_models.Tournament
        exclude = ['id']

class TournamentEventSerializer(serializers.ModelSerializer):

    url_detail = serializers.HyperlinkedIdentityField(
        view_name='api:tournamentEvent-detail',
        lookup_field='id'
        )

    class Meta:
        model = my_models.TournamentEvent
        exclude = ['id']
