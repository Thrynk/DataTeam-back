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
    serializer_class = TennisPlayerSerializer
    model=TennisPlayer
    queryset = model.objects.all().order_by('name')

    def get_queryset(self):
            parms = self.request.GET.dict()
            print(parms)
            name=self.request.GET.get('name')
            if name is not None:
                self.queryset = self.queryset.filter(name=name)
            return self.queryset

class TournamentViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentSerializer
    model=Tournament
    queryset = model.objects.all()

class TournamentEventViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentEventSerializer
    model=TournamentEvent
    queryset = model.objects.all()

class TournamentEventViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentEventSerializer
    model=TournamentEvent
    queryset = model.objects.all()

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    model=Match
    queryset = model.objects.all()

class MatchStatsViewSet(viewsets.ModelViewSet):
    serializer_class = MatchStatsSerializer
    model=MatchStats
    queryset = model.objects.all()

class TennisPlayerStatsViewSet(viewsets.ModelViewSet):
    serializer_class = TennisPlayerStatsSerializer
    model=MatchStats
    queryset = TennisPlayerStats.objects.all()