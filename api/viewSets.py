from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
from django.core import serializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import * 
from .serializers import * 

####### fonctions #######

# renvois les objects en fonctions des parametres de request.GET
def get_query_perso(self):
    queryset=self.model.objects.all().order_by('-id')
    parms = self.request.GET.dict()
    if len(list(parms.keys())) > 0 : # si il y a des parametres dans l'url
        for key in list(parms.keys()):
            if key not in [field.name for field in self.model._meta.fields]: # si le parametre n'est pas le nom d'un un field 
                del parms[key]
        queryset=queryset.filter(**parms) # on filtre notre recherche en fonction des parametres 
    return queryset

# Create your views here.

class TennisPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = TennisPlayerSerializer
    model=TennisPlayer

    def get_queryset(self):
        return get_query_perso(self)
    
    #def create(self, request, *args, **kwargs):
        
    #    parms = self.request.POST.dict() # pour dico de parametres requis

    #    # données en minuscule
    #    for key in list(parms.keys()):
    #        parms[key]=parms[key].lower()

    #    parms_possible =parms.copy() # pour dico de parametres possibles

    #    if len(list(parms.keys())) > 0 : # si il y a des parametres
    #            for key in list(parms.keys()):
    #                if key not in [field.name for field in self.model._meta.fields]: # si le parametre n'est pas le nom d'un un field
    #                    del parms_possible[key]
    #                if  key not in [field.name for field in self.model._meta.fields if field.null==False]: 
    #                    del parms[key]
        
    #    query = self.model.objects.all().filter(**parms) # si il en existe 1 avec les parametres requis
    #    if query.count():
    #        mystatus=status.HTTP_406_NOT_ACCEPTABLE
    #    else:
    #        #self.model.create(**parms)
    #        serializer=self.get_serializer(data=parms_possible) # on creer avec les parametres possibles
    #        if serializer.is_valid():
    #            serializer.save()
    #            mystatus=status.HTTP_201_CREATED
    #        else:
    #            mystatus=status.HTTP_406_NOT_ACCEPTABLE
    #    return Response(parms, status=mystatus, headers=self.get_success_headers(parms))
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class TournamentViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentSerializer
    model=Tournament

    def get_queryset(self):
        return get_query_perso(self)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class TournamentEventViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentEventSerializer
    model=TournamentEvent

    def get_queryset(self):
        return get_query_perso(self)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class TournamentEventViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentEventSerializer
    model=TournamentEvent

    def get_queryset(self):
        return get_query_perso(self)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    model=Match
    
    def get_queryset(self):
        return get_query_perso(self)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class MatchStatsViewSet(viewsets.ModelViewSet):
    serializer_class = MatchStatsSerializer
    model=MatchStats

    def get_queryset(self):
        return get_query_perso(self)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class TennisPlayerStatsViewSet(viewsets.ModelViewSet):
    serializer_class = TennisPlayerStatsSerializer
    model=MatchStats

    def get_queryset(self):
        return get_query_perso(self)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)