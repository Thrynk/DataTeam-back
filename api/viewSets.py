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

    def get_queryset(self):
            queryset=self.model.objects.all().order_by('-id')

            parms = self.request.GET.dict()

            if len(list(parms.keys())) > 0 : # si il y a des parametres dans l'url
                for key in list(parms.keys()):
                    if key not in [field.name for field in self.model._meta.fields]: # si le parametre n'est pas le nom d'un un field 
                        del parms[key]
                queryset=queryset.filter(**parms) # on filtre notre recherche en fonction des parametres 

            return queryset

    def create(self, request, *args, **kwargs):
        parms = self.request.POST.dict() # pour dico de parametres requis

        # données en minuscule
        for key in list(parms.keys()):
            parms[key]=parms[key].lower()

        parms_possible =parms.copy() # pour dico de parametres possibles

        if len(list(parms.keys())) > 0 : # si il y a des parametres
                for key in list(parms.keys()):
                    if key not in [field.name for field in self.model._meta.fields]: # si le parametre n'est pas le nom d'un un field
                        del parms_possible[key]
                    if  key not in [field.name for field in self.model._meta.fields if field.null==False]: 
                        del parms[key]
        
        query = self.model.objects.all().filter(**parms) # si il en existe 1 avec les parametres requis
        if query.count():
            mystatus=status.HTTP_406_NOT_ACCEPTABLE
        else:
            #self.model.create(**parms)
            serializer=self.get_serializer(data=parms_possible) # on creer avec les parametres possibles
            if serializer.is_valid():
                serializer.save()
                mystatus=status.HTTP_201_CREATED
            else:
                mystatus=status.HTTP_406_NOT_ACCEPTABLE
        return Response(parms, status=mystatus, headers=self.get_success_headers(parms))

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