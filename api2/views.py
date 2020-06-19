from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404, FileResponse
#from django.http import Http404
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

from datacollection.meteo2 import recup_meteo

import math

# Create your views here.

# explication du code :
#   chaque views est relier a une url
#   la descriptions de ce que fait la view est donc affichée a coté de l'url dans le fichier url.py

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
            ?page_nombre= : nombre de queryset par page (default=page_nombre_default)
            ?page= : la page dans laquelle nous voulons etre (default=1)

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
                return None, None
        if page_nombre is None:
            page_nombre=page_nombre_default
        else:
            if page_nombre == 'all':
                return queryset,1
            try:
                page_nombre=int(page_nombre)
            except:
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
        ou retourne un status 404 not found
        exemple : ?date='2020-06-01'
        '''
        others_parms=['orderby','page','page_nombre']

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

    def image_taille(self,request,default):
        '''
        parametres: 
            request,
            default,

        retourne la taille de l'image (differentes tailles sont rangées en dossier)
        '''
        tailles_possibles=['16','24','32','48','64']
        taille = request.GET.get('taille')
        if taille is None:
            taille = default
        if taille not in tailles_possibles:
            raise Http404
        else:
            return taille

####################################################################################

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
            'meteo-url': reverse('api2:meteo-list', request=request),
            'city-url': reverse('api2:city-list', request=request),
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

class TennisPlayerFlagView(APIView, PaginationClass, FiltreClass):
    model_class=TennisPlayer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except TennisPlayer.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":self.request}
        queryset = self.get_object(id)
        nationality = queryset.nationality
        FlagName=Flag.objects.get(country_id=nationality).flag_png
        taille=self.image_taille(request,'24')
        img = open('static/Flag/{taille}/{flag_png}'.format(taille=taille,flag_png=FlagName), 'rb')
        return FileResponse(img)

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

    def put(self, request, id, format=None):
        instance = self.get_object(id)
        serializer = self.serializer_class(instance, data=request.POST)#, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

###################################################################################

class CityListView(APIView, PaginationClass, FiltreClass):
    model_class=City
    serializer_class=CityListSerializer

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
        print(queryset_to_show)
        print(serializer.data)
        return Response(data)

class CityDetailView(APIView, PaginationClass, FiltreClass):
    model_class=City
    serializer_class=CityListSerializer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":request}
        queryset = Meteo.objects.all().filter(city=self.get_object(id))
        queryset = self.query_parms(request,queryset,Meteo)
        queryset_to_show, nombre_de_pages = self.paginate_queryset(request, queryset)
        if queryset_to_show is not None:
            serializer = MeteoListSerializer(queryset_to_show, many=True,context=context)
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


class CityMoyenneListView(APIView, PaginationClass, FiltreClass):
    model_class=City
    serializer_class=CityListSerializer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404

    def regroupe_queryset(self,queryset,prm,nb=None):
        """
        regroupe les queryset dans une liste en fonction du parametre prm
        """
        queryset_copie=queryset.all()
        hasattr(queryset_copie.first(),prm)
        L=[]
        while queryset_copie.count():
            if nb is not None:
                ref=getattr(queryset_copie.first(),prm)[0:nb]
                filtre={"{}__icontains".format(prm):ref}
            else:
                ref=getattr(queryset_copie.first(),prm)
                filtre={"{}".format(prm):ref}
            q = queryset_copie.filter(**filtre)
            L.append(q)
            queryset_copie = queryset_copie.exclude(**filtre)
        return L

    def get(self, request, id, format=None):
        context={"request":request}
        queryset = Meteo.objects.all().filter(city=self.get_object(id))
        queryset = self.query_parms(request,queryset,Meteo)

        List=self.regroupe_queryset(queryset,"date_time",10)
        L=[]

        data_a_moyenner=["temperature", "humidity", "precipitation"]

        for queryset in List:
            data={
                "heures":query.count(),
                "date_time": query.first().date_time,
                "location_latitude": query.first().location_latitude,
                "location_longitude": query.first().location_longitude,
                "temperature": 0,
                "humidity": 0,
                "precipitation": 0,
                "url_meteo_image":"",
                }
            for q in queryset:
                for i in data_a_moyenner:
                    data[i] += getattr(q,i)
                #data["temperature"]+=q.temperature
                #data["humidity"]+=q.humidity
                #data["precipitation"]+=q.precipitation

            for i in data_a_moyenner:
                    data[i] = math.ceil(data[i]/data["heures"])
            #data["temperature"]=math.ceil(data["temperature"]/data["heures"])
            #data["humidity"]=math.ceil(data["humidity"]/data["heures"])
            #data["precipitation"]=math.ceil(data["precipitation"]/data["heures"])

            humidity=data["humidity"]
            if humidity>80 and humidity<100:
                image_name="pluie"
            elif humidity>0 and humidity<30:
                image_name="soleil"
            else:
                image_name="soleil_nuage"
            data["url_meteo_image"]=reverse('api2:meteo-image-name', kwargs={"image_name":image_name}, request=request)
            L.append(data)

        return Response(L)


#class CityImageView(APIView, PaginationClass, FiltreClass):
#    model_class=Meteo

#    def get_object(self, id):
#        try:
#            return self.model_class.objects.get(id=id)
#        except TennisPlayer.DoesNotExist:
#            raise Http404

#    def get(self, request, id, format=None):
#        context={"request":self.request}
#        queryset = self.get_object(id)

#        humidity=queryset.humidity
#        temperature=queryset.temperature
#        precipitation=queryset.precipitation

#        switch={
#            "pluie":"pluie.png",
#            "soleil":"soleil.png",
#            "soleil_nuage":"soleil_nuage.png",
#            }
#        if humidity>80 and humidity<100:
#            image_name="pluie"
#        elif humidity>0 and humidity<30:
#            image_name="soleil"
#        else:
#            image_name="soleil_nuage"

#        img = open('static/meteo/{image_name}'.format(image_name=switch[image_name]), 'rb')
        return FileResponse(img)

###################################################################################

class MeteoListView(APIView, PaginationClass, FiltreClass):
    model_class=Meteo
    serializer_class=MeteoListSerializer

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

class MeteoDetailView(APIView):
    model_class=Meteo
    serializer_class=MeteoDetailSerializer

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

class MeteoUpdateView(APIView):
    model_class=Meteo

    def post(self, request, format=None):
        context={"request":request}
        import geopy.distance
        from datetime import datetime, timedelta

        default_distance=50
        delta_default = timedelta(
            days=0,
            seconds=0,
            microseconds=0,
            milliseconds=0,
            minutes=0,
            hours=1,
            weeks=0
            )
        #data=request.POST.dict()
        data=request.data

        longitude=data["longitude"]
        latitude=data["latitude"]

        cities = City.objects.all().order_by('location_longitude', 'location_latitude')

        for city in cities:
            coords_1 = (latitude, longitude)
            coords_2 = (city.location_latitude, city.location_longitude)
            print(coords_1,coords_2)
            distance = geopy.distance.vincenty(coords_1, coords_2).km
            if distance<=default_distance:
                print(datetime.now())
                print(city.last_load.replace(tzinfo=None))
                print(delta_default)
                print(datetime.now() - city.last_load.replace(tzinfo=None))
                print(datetime.now() - city.last_load.replace(tzinfo=None) > delta_default)
                if datetime.now() - city.last_load.replace(tzinfo=None) > delta_default:
                    city = recup_meteo(latitude,longitude,city)
                queryset=Meteo.objects.filter(location_latitude=city.location_latitude, location_longitude=city.location_longitude)
                serilizer=MeteoListSerializer(queryset, many=True,context=context)
                return Response({"city_id":city.id})
                return Response(serilizer.data)

        city = recup_meteo(latitude,longitude)
        queryset=Meteo.objects.filter(location_latitude=city.location_latitude, location_longitude=city.location_longitude)
        serilizer=MeteoListSerializer(queryset, many=True,context=context)
        return Response({"city_id":city.id})
        return Response(serilizer.data)


class MeteoImageView(APIView, PaginationClass, FiltreClass):
    model_class=Meteo

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except TennisPlayer.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":self.request}
        queryset = self.get_object(id)

        humidity=queryset.humidity
        temperature=queryset.temperature
        precipitation=queryset.precipitation

        switch={
            "pluie":"pluie.png",
            "soleil":"soleil.png",
            "soleil_nuage":"soleil_nuage.png",
            }
        if humidity>80 and humidity<100:
            image_name="pluie"
        elif humidity>0 and humidity<30:
            image_name="soleil"
        else:
            image_name="soleil_nuage"

        img = open('static/meteo/{image_name}'.format(image_name=switch[image_name]), 'rb')
        return FileResponse(img)

####################################################################################

class MeteoImageNameView(APIView, PaginationClass, FiltreClass):
    model_class=Meteo

    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except TennisPlayer.DoesNotExist:
            raise Http404

    def get(self, request, image_name, format=None):
        switch={
            "pluie":"pluie.png",
            "soleil":"soleil.png",
            "soleil_nuage":"soleil_nuage.png",
            }
        img = open('static/meteo/{image_name}'.format(image_name=switch[image_name]), 'rb')
        return FileResponse(img)

####################################################################################

#class LocalisationView(APIView):

#    def post(self, request):
#        a=0

####################################################################################

#class MeteotestView(APIView):

#    def post(self, request):
#        a=request.POST.dict()
#        return Response(a)

####################################################################################


