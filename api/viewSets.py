from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
from django.core import serializers
from django.db.models import Q

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .models import * 
from .serializers import * 

# ----- fonctions ----- #

# renvois les objects en fonctions des parametres de request.GET
def query_parms(self,query,model_class):
    others_parms=['orderby, page']
    fieldsNames=[field.name for field in model_class._meta.fields] # exemple ['name','firstname']

    orderby = self.request.GET.get('orderby')
    if orderby is None:
        orderby = 'id'

    queryset=query.order_by(orderby)
    parms = self.request.GET.dict()

    if len(list(parms.keys())) > 0 : # si il y a des parametres dans l'url
        for key in list(parms.keys()):
        #    if key not in fieldsNames: # si le parametre n'est pas le nom d'un un field 
        #        del parms[key]
            try:
                queryset=queryset.filter(**{key:parms[key]}) # on filtre notre recherche en fonction des parametres 
            except:
                queryset=queryset
    return queryset

# Create your views here.

# un ViewSets definie le comportement d'une view

class TennisPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = TennisPlayerSerializer
    model_class=TennisPlayer

    queryset=model_class.objects.all()

    lookup_field = 'id'

    # object à renvoyer en json
    def get_queryset(self):
        return query_parms(self, self.queryset, self.model_class)

    # revois les objects en liste
    # fonction appellee lors d'un request GET (TennisPlayer/)
    def list(self, request, *args, **kwargs):
        context={"request":self.request}
        queryset=self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context=context)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True, context=context)
        return Response(serializer.data)
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

    @action(detail=True, methods=['get'])
    def match(self, request, id, pk=None):
        context={"request":self.request}

        serializer_class = MatchSerializer
        model_class = Match

        queryset = model_class.objects.all().filter(
            Q(loser=id)|
            Q(winner=id)
            )
        queryset=query_parms(self,queryset, model_class)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = serializer_class(page, many=True, context=context)
            return self.get_paginated_response(serializer.data)
        serializer = serializer_class(queryset, many=True, context=context)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def stats(self, request, id, pk=None):
        return redirect('api:tennisPlayerStats-detail',id=id)


class TournamentViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentSerializer
    model_class=Tournament

    queryset=model_class.objects.all()

    lookup_field = 'id'


    def get_queryset(self):
        return query_parms(self, self.queryset, self.model_class)

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
    model_class=TournamentEvent

    queryset=model_class.objects.all()

    lookup_field = 'id'


    def get_queryset(self):
        return query_parms(self, self.queryset, self.model_class)

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
    model_class=TournamentEvent

    queryset=model_class.objects.all()

    lookup_field = 'id'


    def get_queryset(self):
        return query_parms(self, self.queryset, self.model_class)

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
    model_class=Match

    lookup_field = 'id'

    queryset=model_class.objects.all()
    
    def get_queryset(self):
        return query_parms(self, self.queryset, self.model_class)

    #@action(detail=False, methods=['get'])
    #def year_filter(self, request, pk=None):
    #    queryset = self.model_class.objects.all().filter(Q(date__gte='2018-06-01'))
    #    #queryset = self.model_class.objects.all()
    #    page = self.paginate_queryset(queryset, self.model_class)
    #    if page is not None:
    #        serializer = self.get_serializer(page, many=True)
    #        return self.get_paginated_response(serializer.data)
    #    serializer = self.get_serializer(queryset, many=True)
    #    return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        context={"request":self.request}
        queryset=self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context=context)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True, context=context)
        return Response(serializer.data)
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=['get'])
    def stats(self, request, id, pk=None):
        return redirect('api:matchStats-detail',id=id)


class MatchStatsViewSet(viewsets.ModelViewSet):
    serializer_class = MatchStatsSerializer
    model_class=MatchStats

    queryset=model_class.objects.all()

    lookup_field = 'id'


    def get_queryset(self):
        return query_parms(self, self.queryset, self.model_class)

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
    model_class=MatchStats

    lookup_field = 'id'

    queryset=model_class.objects.all()


    def get_queryset(self):
        return query_parms(self, self.queryset, self.model_class)

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

class AnecdoteViewSet(viewsets.ModelViewSet):
    serializer_class = AnecdoteSerializer
    model_class=Anecdote

    lookup_field = 'id'

    queryset=model_class.objects.all()


    def get_queryset(self):
        return query_parms(self, self.queryset, self.model_class)

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