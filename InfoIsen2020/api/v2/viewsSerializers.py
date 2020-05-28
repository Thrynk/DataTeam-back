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
from __divers__.perso import Button,URL
from __divers__.decorators import logout_required

from .serializers import UserSerializer

########

class usersListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

@csrf_exempt
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)
        return JsonResponse(userSerializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        userSerializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(userSerializer.data, status=201)
        return JsonResponse(userSerializer.errors, status=400)