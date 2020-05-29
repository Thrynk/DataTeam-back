from rest_framework import serializers

#from .models import Hero
from django.contrib.auth.models import User
from api import models as my_models


#class UserSerializer(serializers.HyperlinkedModelSerializer):
#class UserSerializer(serializers.Serializer):
class TennisPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models.TennisPlayer
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models.Match
        fields = '__all__'

class MatchStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models.MatchStats
        fields = '__all__'

class TennisPlayerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models.TennisPlayerStats
        fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models.Tournament
        fields = '__all__'

class TournamentEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models.TournamentEvent
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']