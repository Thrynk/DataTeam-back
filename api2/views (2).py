from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import * 
from .serializers import * 

import math

# Create your views here.

####################################################################################
class TennisPlayerListView(APIView):
    model_class=TennisPlayer
    serializer_class=TennisPlayerListSerializer

    def get(self, request, format=None):
        context={"request":request}

        page_nombre=request.GET.get('page_nombre')
        page=request.GET.get('page')

        if page is None:
            page=1
        else:
            try:
                page=int(page)
            except:
                data={
                    "error in parameters":"page must be a int()",
                    }
                return Response(data)
        if page_nombre is None:
            page_nombre=10
        else:
            try:
                page_nombre=int(page_nombre)
            except:
                data={
                    "error in parameters":"page_nombre must be a int()",
                    }
                return Response(data)
        min=page*page_nombre-page_nombre
        max=page*page_nombre
        print(min,max)
            
        queryset = self.model_class.objects.all()
        queryset_to_show = queryset[min:max]
        serializer = self.serializer_class(queryset_to_show, many=True,context=context)

        data={
            "count":queryset.count(),
            "number of pages":math.ceil(queryset.count()/page_nombre),
            "results":serializer.data
            }
        return Response(data)

    #def post(self, request, format=None):
    #    serializer = TennisPlayerSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TennisPlayerDetailView(APIView):
    model_class=TennisPlayer
    serializer_class=TennisPlayerDetailSerializer

    def get_object(self, id):
        try:
            return self.model_class.objects.get(pk=id)
        except TennisPlayer.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        context={"request":request}
        queryset = self.get_object(id)
        serializer = self.serializer_class(queryset,context=context)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = TennisPlayerSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects = self.get_object(pk)
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

####################################################################################
class TournamentListView(APIView):

    def get(self, request, format=None):
        objects = Tournament.objects.all()
        serializer = TournamentSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TournamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TournamentDetailView(APIView):

    def get_object(self, pk):
        try:
            return Tournament.objects.get(pk=pk)
        except Tournament.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = TournamentSerializer(objects)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = TournamentSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects = self.get_object(pk)
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

####################################################################################
class TournamentEventListView(APIView):

    def get(self, request, format=None):
        objects = TournamentEvent.objects.all()
        serializer = TournamentEventSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TournamentEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TournamentEventDetailView(APIView):

    def get_object(self, pk):
        try:
            return TournamentEvent.objects.get(pk=pk)
        except TournamentEvent.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = TournamentEventSerializer(objects)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = TournamentEventSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects = self.get_object(pk)
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

####################################################################################
class MatchListView(APIView):

    def get(self, request, format=None):
        objects = Match.objects.all()
        serializer =MatchSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatchDetailView(APIView):

    def get_object(self, pk):
        try:
            return Match.objects.get(pk=pk)
        except Match.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = MatchSerializer(objects)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = MatchSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects = self.get_object(pk)
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

###################################################################################
class MatchStatsListView(APIView):

    def get(self, request, format=None):
        objects = MatchStats.objects.all()
        serializer =MatchStatsSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MatchStatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatchStatsDetailView(APIView):

    def get_object(self, pk):
        try:
            return MatchStats.objects.get(pk=pk)
        except MatchStats.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = MatchStatsSerializer(objects)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = MatchStatsSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects = self.get_object(pk)
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

###################################################################################
class TennisPlayerStatsListView(APIView):

    def get(self, request, format=None):
        objects = TennisPlayerStats.objects.all()
        serializer = TennisPlayerStatsSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TennisPlayerStatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TennisPlayerStatsDetailView(APIView):

    def get_object(self, pk):
        try:
            return TennisPlayerStats.objects.get(pk=pk)
        except TennisPlayerStats.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = TennisPlayerStatsSerializer(objects)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = TennisPlayerStatsSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects = self.get_object(pk)
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)