from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import Http404
from django import http
from django.core.paginator import Paginator
from django.core import serializers
from django.db.models import Q

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import * 
from .serializers import * 

import math

# Create your views here.

###################################################################################

class PaginationClass:
    def paginate_queryset(self, request, queryset, page_nombre_default=10):
        """
        description:
            pagine le query en fonction des parametres de la requete : 

        parametres de la fonction :
            request : la requete
            queryset : le queryset a paginer
            page_nombre_default = nombre de queryset par page (default=10)

        parametres de la requete:
            page_nombre : nombre de queryset par page (default=page_nombre_default)
            page : la page dans laquelle nous voulons etre (default=1)

        retourne :
            None : en cas d'erreurs dans les parametres
            queryset, nombre_de_page : sans erreurs
        """
        page_nombre=request.GET.get('page_nombre')
        page=request.GET.get('page')
        if page is None:
            page=1
        else:
            try:
                page=int(page)
            except:
                #data={
                #    "error in parameters":"page must be a int()",
                #    }
                #return Response(data)
                return None, None
        if page_nombre is None:
            page_nombre=page_nombre_default
        else:
            if page_nombre == 'all':
                return queryset,1
            try:
                page_nombre=int(page_nombre)
            except:
                #data={
                #    "error in parameters":"page_nombre must be a int()",
                #    }
                #return Response(data)
                return None, None
        min=page*page_nombre-page_nombre
        max=page*page_nombre
        nombre_de_pages=math.ceil(queryset.count()/page_nombre)
        return queryset[min:max],nombre_de_pages

class FiltreClass:
    def List(self, List,var):
        L=[('{var}__'+key).format(var=var) for key in List]+['{var}'.format(var=var)]
        #print(L)
        return L

    def query_parms(self, request, queryset, model_class):
        '''
        parametres: 
            request,
            query,
            model_class,

        retourne le queryset filtrer en fonction des parametres de l'url
        '''
        others_parms=['orderby','page','page_nombre']

        fieldsNames=[field.name for field in model_class._meta.fields] # exemple ['name','firstname']

        orderby = request.GET.get('orderby')
        if orderby is None:
            orderby = 'id'
        queryset=queryset.order_by(orderby)

        parms = request.GET.dict()
        if len(list(parms.keys())) > 0 : # si il y a des parametres dans l'url
            for key_parms in list(parms.keys()):
                if key_parms not in others_parms:
                    try:
                        queryset=queryset.filter(**{key_parms:parms[key_parms]}) # on filtre notre recherche en fonction des parametres 
                    except:
                        raise Http404
        return queryset

class ApiRootListView(APIView):
    
    def get(self, request, format=None):
        data = {
            'tennisPlayer-url': reverse('api2:tennisPlayer-list', request=request),
            'match-url': reverse('api2:match-list', request=request),
            'tennisPlayerStats-url': reverse('api2:tennisPlayerStats-list', request=request),
            'matchStats-url': reverse('api2:matchStats-list', request=request),
            'tournament-url': reverse('api2:tournament-list', request=request),
            'tournamentEvent-url': reverse('api2:tournamentEvent-list', request=request),
            'anecdote-url': reverse('api2:anecdote-list', request=request),
        }
        return Response(data)

####################################################################################

class TennisPlayerListView(APIView, PaginationClass, FiltreClass):
    model_class=TennisPlayer
    serializer_class=TennisPlayerListSerializer

    def get(self, request, format=None):
        context={"request":request}
        queryset = self.model_class.objects.all()

        queryset = self.query_parms(request,queryset,self.model_class)

        queryset_to_show, nombre_de_pages = self.paginate_queryset(request, queryset)
        if queryset_to_show is not None:
            serializer = self.serializer_class(queryset_to_show, many=True,context=context)
            data={
                "count":queryset.count(),
                "number of pages":nombre_de_pages,
                "results":serializer.data
                }
        else:
            data={
                "error in parameters":"page_nombre and page must be int()",
                }
        return Response(data)

class TennisPlayerDetailView(APIView):
    model_class=TennisPlayer
    serializer_class=TennisPlayerDetailSerializer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":request}
        queryset = self.get_object(id)
        serializer = self.serializer_class(queryset,context=context)
        return Response(serializer.data)

class TennisPlayerMatchView(APIView, PaginationClass, FiltreClass):
    model_class=TennisPlayer
    serializer_class=MatchListSerializer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except TennisPlayer.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":self.request}
        serializer_class = self.serializer_class
        model_class = Match
        queryset = model_class.objects.all().filter(
            Q(loser=id)|
            Q(winner=id)
            )
        queryset = self.query_parms(request,queryset,model_class)
        queryset_to_show, nombre_de_pages = self.paginate_queryset(request, queryset)
        if queryset_to_show is not None:
            serializer = serializer_class(queryset_to_show, many=True,context=context)
            data={
                "count":queryset.count(),
                "number of pages":nombre_de_pages,
                "results":serializer.data
                }
        else:
            data={
                "error in parameters":"page_nombre and page must be int()",
                }
        return Response(data)

class TennisPlayerStatsView(APIView):

    def get(self, request, id, format=None):
        return redirect('api2:tennisPlayerStats-detail',id=id)

####################################################################################

class TournamentListView(APIView, PaginationClass, FiltreClass):
    model_class=Tournament
    serializer_class=TournamentListSerializer

    def get(self, request, format=None):
        context={"request":request}
        queryset = self.model_class.objects.all()
        queryset = self.query_parms(request,queryset,self.model_class)
        queryset_to_show, nombre_de_pages = self.paginate_queryset(request, queryset)
        if queryset_to_show is not None:
            serializer = self.serializer_class(queryset_to_show, many=True,context=context)
            data={
                "count":queryset.count(),
                "number of pages":nombre_de_pages,
                "results":serializer.data
                }
        else:
            data={
                "error in parameters":"page_nombre and page must be int()",
                }
        return Response(data)

class TournamentDetailView(APIView):
    model_class=Tournament
    serializer_class=TournamentDetailSerializer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":request}
        queryset = self.get_object(id)
        serializer = self.serializer_class(queryset,context=context)
        return Response(serializer.data)

####################################################################################

class TournamentEventListView(APIView, PaginationClass, FiltreClass):
    model_class=TournamentEvent
    serializer_class=TournamentEventListSerializer

    def get(self, request, format=None):
        context={"request":request}
        queryset = self.model_class.objects.all()
        queryset = self.query_parms(request,queryset,self.model_class)
        queryset_to_show, nombre_de_pages = self.paginate_queryset(request, queryset)
        if queryset_to_show is not None:
            serializer = self.serializer_class(queryset_to_show, many=True,context=context)
            data={
                "count":queryset.count(),
                "number of pages":nombre_de_pages,
                "results":serializer.data
                }
        else:
            data={
                "error in parameters":"page_nombre and page must be int()",
                }
        return Response(data)

class TournamentEventDetailView(APIView):
    model_class=TournamentEvent
    serializer_class=TournamentEventDetailSerializer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":request}
        queryset = self.get_object(id)
        serializer = self.serializer_class(queryset,context=context)
        return Response(serializer.data)

####################################################################################

class MatchListView(APIView, PaginationClass, FiltreClass):
    model_class=Match
    serializer_class=MatchListSerializer

    def get(self, request, format=None):
        context={"request":request}
        queryset = self.model_class.objects.all()
        queryset = self.query_parms(request,queryset,self.model_class)
        queryset_to_show, nombre_de_pages = self.paginate_queryset(request, queryset)
        if queryset_to_show is not None:
            serializer = self.serializer_class(queryset_to_show, many=True,context=context)
            data={
                "count":queryset.count(),
                "number of pages":nombre_de_pages,
                "results":serializer.data
                }
        else:
            data={
                "error in parameters":"page_nombre and page must be int()",
                }
        return Response(data)

class MatchDetailView(APIView):
    model_class=Match
    serializer_class=MatchDetailSerializer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":request}
        queryset = self.get_object(id)
        serializer = self.serializer_class(queryset,context=context)
        return Response(serializer.data)

class MatchStatsView(APIView):

    def get(self, request, id, format=None):
        return redirect('api2:matchStats-detail',id=id)

###################################################################################

class MatchStatsListView(APIView, PaginationClass, FiltreClass):
    model_class=MatchStats
    serializer_class=MatchStatsListSerializer

    def get(self, request, format=None):
        context={"request":request}
        queryset = self.model_class.objects.all()
        queryset = self.query_parms(request,queryset,self.model_class)
        queryset_to_show, nombre_de_pages = self.paginate_queryset(request, queryset)
        if queryset_to_show is not None:
            serializer = self.serializer_class(queryset_to_show, many=True,context=context)
            data={
                "count":queryset.count(),
                "number of pages":nombre_de_pages,
                "results":serializer.data
                }
        else:
            data={
                "error in parameters":"page_nombre and page must be int()",
                }
        return Response(data)


class MatchStatsDetailView(APIView):
    model_class=MatchStats
    serializer_class=MatchStatsDetailSerializer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":request}
        queryset = self.get_object(id)
        serializer = self.serializer_class(queryset,context=context)
        return Response(serializer.data)

###################################################################################

class TennisPlayerStatsListView(APIView, PaginationClass, FiltreClass):
    model_class=TennisPlayerStats
    serializer_class=TennisPlayerStatsListSerializer

    def get(self, request, format=None):
        context={"request":request}
        queryset = self.model_class.objects.all()
        queryset = self.query_parms(request,queryset,self.model_class)
        queryset_to_show, nombre_de_pages = self.paginate_queryset(request, queryset)
        if queryset_to_show is not None:
            serializer = self.serializer_class(queryset_to_show, many=True,context=context)
            data={
                "count":queryset.count(),
                "number of pages":nombre_de_pages,
                "results":serializer.data
                }
        else:
            data={
                "error in parameters":"page_nombre and page must be int()",
                }
        return Response(data)

class TennisPlayerStatsDetailView(APIView):
    model_class=TennisPlayerStats
    serializer_class=TennisPlayerStatsDetailSerializer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":request}
        queryset = self.get_object(id)
        serializer = self.serializer_class(queryset,context=context)
        return Response(serializer.data)

###################################################################################

class AnecdoteListView(APIView, PaginationClass, FiltreClass):
    model_class=Anecdote
    serializer_class=AnecdoteListSerializer

    def get(self, request, format=None):
        context={"request":request}
        queryset = self.model_class.objects.all()
        queryset = self.query_parms(request,queryset,self.model_class)
        queryset_to_show, nombre_de_pages = self.paginate_queryset(request, queryset)
        if queryset_to_show is not None:
            serializer = self.serializer_class(queryset_to_show, many=True,context=context)
            data={
                "count":queryset.count(),
                "number of pages":nombre_de_pages,
                "results":serializer.data
                }
        else:
            data={
                "error in parameters":"page_nombre and page must be int()",
                }
        return Response(data)

class AnecdoteDetailView(APIView):
    model_class=Anecdote
    serializer_class=AnecdoteDetailSerializer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":request}
        queryset = self.get_object(id)
        serializer = self.serializer_class(queryset,context=context)
        return Response(serializer.data)

###################################################################################
