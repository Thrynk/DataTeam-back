from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from __divers__.perso import Button, URL
from __divers__.decorators import logout_required

# Create your views here.

# Create your views here.

@login_required(login_url=URL.login)
def index(request):
    navbarButtonsList=[Button('Home',URL.home,True),Button('Logout','appUser.logout')]
    context={
        'navbarButtonsList':navbarButtonsList,
        }
    return render(request,'homeconnecte.html',context) 
