from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout, login as auth_login

from api.forms import LoginForm, RegisterForm

from django.http import QueryDict
from django.http import JsonResponse

import api.models as my_models


# Create your views here.

#@logout_required(redirect_url_name=URL.home)
@csrf_exempt
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.process(request)
        else:
            context={
               "success":"0",
               }
            return JsonResponse(context)
    return redirect('api.v1.user_info')
    
#@logout_required(redirect_url_name=URL.home)
@csrf_exempt
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.process(request)
            if user is not None:
                auth_login(request,user)
        else:
            context={
                "success":"0",
                }
            return JsonResponse(context)
    return redirect('api.v1.user_info')

@csrf_exempt
def logout(request):
    auth_logout(request)
    return redirect('api.v1.user_info')

@csrf_exempt
def user_info(request):
    context={
        "success":"1",
        "user_is_authenticated":"0",
        }
    username=request.user.username
    if request.user.is_authenticated:
        context["user_is_authenticated"]="1"
        context["username"]=username
    return JsonResponse(context)

###############################################

class TennisPlayerView:

    def TennisPlayer_list(resquest):
        TennisPlayers = my_models.TennisPlayer.objects.all().order_by('name')
        print(list(TennisPlayers))



