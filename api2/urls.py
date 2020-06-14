"""azerty URL Configuration

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
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views
#from . import viewSets

urlpatterns = [
    path('', views.ApiRootListView.as_view(), name='ApiUrlList'),

    path('tennisPlayer/', views.TennisPlayerListView.as_view(), name='tennisPlayer-list'),
    path('tennisPlayer/<str:id>/', views.TennisPlayerDetailView.as_view(), name='tennisPlayer-detail'),
    path('tennisPlayer/<str:id>/match/', views.TennisPlayerMatchView.as_view(), name='tennisPlayer-match'),
    path('tennisPlayer/<str:id>/stats/', views.TennisPlayerStatsView.as_view(), name='tennisPlayer-stats'),

    path('tennisPlayerStats/', views.TennisPlayerStatsListView.as_view(), name='tennisPlayerStats-list'),
    path('tennisPlayerStats/<str:id>/', views.TennisPlayerStatsDetailView.as_view(), name='tennisPlayerStats-detail'),

    path('match/', views.MatchListView.as_view(), name='match-list'),
    path('match/<str:id>/', views.MatchDetailView.as_view(), name='match-detail'),
    path('match/<str:id>/stats/', views.MatchStatsView.as_view(), name='match-stats'),

    path('matchStats/', views.MatchStatsListView.as_view(), name='matchStats-list'),
    path('matchStats/<str:id>/', views.MatchStatsDetailView.as_view(), name='matchStats-detail'),

    path('tournament/', views.TournamentListView.as_view(), name='tournament-list'),
    path('tournament/<str:id>/', views.TournamentDetailView.as_view(), name='tournament-detail'),

    path('tournamentEvent/', views.TournamentEventListView.as_view(), name='tournamentEvent-list'),
    path('tournamentEvent/<str:id>/', views.TournamentEventDetailView.as_view(), name='tournamentEvent-detail'),

    path('anecdote/', views.AnecdoteListView.as_view(), name='anecdote-list'),
    path('anecdote/<str:id>/', views.AnecdoteDetailView.as_view(), name='anecdote-detail'),

    path('meteo/', views.MeteoListView.as_view(), name='meteo-list'),
    path('meteo/<str:id>/', views.MeteoDetailView.as_view(), name='meteo-detail'),

    path('flag/<str:taille>/<str:Country_code>', views.FlagDetailView.as_view(), name='flag-detail'),



]
