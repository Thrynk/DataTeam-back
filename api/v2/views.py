from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import QueryDict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
import json

from api.forms import LoginForm, RegisterForm


from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions


from api import models as my_models
from . import serializers as my_serialisers

########

@api_view(['GET', 'POST'])
def tennisPlayer_list(request):
    if request.method == 'GET':
        TennisPlayers = my_models.TennisPlayer.objects.all()
        serializer = my_serialisers.TennisPlayerSerializer(TennisPlayers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = my_serialisers.TennisPlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        TennisPlayers = User.objects.all()
        serializer = my_serialisers.UserSerializer(TennisPlayers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = my_serialisers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE']) 
def tennisPlayer_detail(request, pk):
    try:
        tennisPlayer = my_models.TennisPlayer.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = my_serialisers.TennisPlayerSerializer(tennisPlayer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(tennisPlayer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tennisPlayer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

