from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm
from __divers__.perso import Button, URL
from __divers__.decorators import logout_required

# Create your views here.

# Create your views here.

def index(request):
    return redirect(URL.login) 

@logout_required(redirect_url_name=URL.home)
def register(request):
    navbarButtonsList=[Button('Home',URL.home),Button('Login',URL.login),Button('Register',URL.register,True)]

    #Do something for anonymous users...
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.process()
            messages.success(request, 'Account created successfully')
            return redirect(URL.login)
    else:
        form = RegisterForm()
    context={
        "form":form,
        'navbarButtonsList':navbarButtonsList,
        }
    return render(request,'register.html',context)
    
@logout_required(redirect_url_name=URL.home)
def login(request):
        navbarButtonsList=[Button('Home',URL.home),Button('Login',URL.login,True),Button('Register',URL.register)]

        #Do something for anonymous users...
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                user = form.process(request)
                if user is not None:
                    auth_login(request,user)
                    messages.success(request,'user login successfully ')
                    return redirect(URL.home)
                else:
                    messages.error(request,'user login failed')
        else:
            form = LoginForm()
        context={
            "form":form,
            'navbarButtonsList':navbarButtonsList,
            }
        return render(request,'login.html',context)

def logout(request):
    auth_logout(request)
    return redirect(URL.home)