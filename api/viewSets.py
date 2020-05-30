from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import * 
from .serializers import * 

# Create your views here.

class TennisPlayerViewSet(viewsets.ModelViewSet):
    queryset = TennisPlayer.objects.all()
    serializer_class = TennisPlayerSerializer

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class TournamentEventViewSet(viewsets.ModelViewSet):
    queryset = TournamentEvent.objects.all()
    serializer_class = TournamentEventSerializer

class TournamentEventViewSet(viewsets.ModelViewSet):
    queryset = TournamentEvent.objects.all()
    serializer_class = TournamentEventSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchStatsViewSet(viewsets.ModelViewSet):
    queryset = MatchStats.objects.all()
    serializer_class = MatchStatsSerializer

class TennisPlayerStatsViewSet(viewsets.ModelViewSet):
    queryset = TennisPlayerStats.objects.all()
    serializer_class = TennisPlayerStatsSerializer