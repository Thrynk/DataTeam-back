"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    #path('', include(router.urls), name='api.v1.router'),

    path('login/', views.login, name='api.v1.login'),
    path('register/', views.register, name='api.v1.register'),
    path('logout/', views.logout, name='api.v1.logout'),
    path('user_info/', views.user_info, name='api.v1.user_info'),

    path('TennisPlayer_list/', views.TennisPlayerView.TennisPlayer_list, name='api.v1.TennisPlayer_list'),


]