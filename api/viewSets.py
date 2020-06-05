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

# ----- fonctions ----- #

# renvois les objects en fonctions des parametres de request.GET
def get_query_perso(self,order):
    queryset=self.model.objects.all().order_by(order)
    parms = self.request.GET.dict()
    if len(list(parms.keys())) > 0 : # si il y a des parametres dans l'url
        for key in list(parms.keys()):
            if key not in [field.name for field in self.model._meta.fields]: # si le parametre n'est pas le nom d'un un field 
                del parms[key]
        queryset=queryset.filter(**parms) # on filtre notre recherche en fonction des parametres 
    return queryset

# Create your views here.

# un ViewSets definie le comportement d'une view

class TennisPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = TennisPlayerSerializer
    model=TennisPlayer

    lookup_field = 'id'

    # object à renvoyer en json
    def get_queryset(self):
        return get_query_perso(self,order='name')
    
    # revois les objects en liste
    # fonction appellee lors d'un request GET (TennisPlayer/)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # fonction appellee lors d'un request POST (TennisPlayer/)
    def create(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # fonction appellee lors d'un request PUT (TennisPlayer/<id>)
    def update(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # fonction appellee lors d'un request DELETE (TennisPlayer/<id>)
    def destroy(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # fonction appellee lors d'un request GET (TennisPlayer/<id>)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class TournamentViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentSerializer
    model=Tournament

    lookup_field = 'id'


    def get_queryset(self):
        return get_query_perso(self,order='-id')

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

    lookup_field = 'id'


    def get_queryset(self):
        return get_query_perso(self,order='-date')

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

    lookup_field = 'id'


    def get_queryset(self):
        return get_query_perso(self,order='-date')

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

    lookup_field = 'id'

    
    def get_queryset(self):
        return get_query_perso(self, order='-date')

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

    lookup_field = 'id'


    def get_queryset(self):
        return get_query_perso(self,order='match')

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

    lookup_field = 'id'


    def get_queryset(self):
        return get_query_perso(self, order='id')

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