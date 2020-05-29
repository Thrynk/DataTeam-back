from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import * 
from .serializers import * 

# Create your views here.

def apiOverview(request):
    return JsonResponse('TEST', safe=False)

####################################################################################
class TennisPlayerList(APIView):

    def get(self, request, format=None):
        objects = TennisPlayer.objects.all()
        serializer = TennisPlayerSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TennisPlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TennisPlayerDetail(APIView):

    def get_object(self, pk):
        try:
            return TennisPlayer.objects.get(pk=pk)
        except TennisPlayer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = TennisPlayerSerializer(objects)
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
class TournamentList(APIView):

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

class TournamentDetail(APIView):

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
class TournamentEventList(APIView):

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

class TournamentEventDetail(APIView):

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
class MatchList(APIView):

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

class MatchDetail(APIView):

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
class MatchStatsList(APIView):

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

class MatchStatsDetail(APIView):

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
class TennisPlayerStatsList(APIView):

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

class TennisPlayerStatsDetail(APIView):

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