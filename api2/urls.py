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

    path('tennisPlayer/', views.TennisPlayerListView.as_view(), name='tennisPlayer-list'), # liste tous les joueurs de tennis
    path('tennisPlayer/<str:id>/', views.TennisPlayerDetailView.as_view(), name='tennisPlayer-detail'), # affiche les detail du joueur n°id
    path('tennisPlayer/<str:id>/flag/', views.TennisPlayerFlagView.as_view(), name='tennisPlayer-flag'), # renvois le drapeaux du pays du joueur
    path('tennisPlayer/<str:id>/match/', views.TennisPlayerMatchView.as_view(), name='tennisPlayer-match'), # liste tous les matchs du joueur
    path('tennisPlayer/<str:id>/stats/', views.TennisPlayerStatsView.as_view(), name='tennisPlayer-stats'), # liste toutes les stats du joueur

    #path('tennisPlayerStats/', views.TennisPlayerStatsListView.as_view(), name='tennisPlayerStats-list'), # liste les stats de tous les joueurs
    #path('tennisPlayerStats/<str:id>/', views.TennisPlayerStatsDetailView.as_view(), name='tennisPlayerStats-detail'), # liste les stats du joueur n°id

    path('match/', views.MatchListView.as_view(), name='match-list'), # liste tous les matchs
    path('match/<str:id>/', views.MatchDetailView.as_view(), name='match-detail'), # affiche les detail du match n°id
    path('match/<str:id>/stats/', views.MatchStatsView.as_view(), name='match-stats'), # liste toutes les stats du match

    path('match/<str:id>/tennisplayersstats/', views.MatchPlayersStatsView.as_view(), name='match-tennisplayersstats'), # liste toutes les stats des deux joueurs du match

    path('matchStats/', views.MatchStatsListView.as_view(), name='matchStats-list'), # liste les stats de tous les matchs
    path('matchStats/<str:id>/', views.MatchStatsDetailView.as_view(), name='matchStats-detail'), # liste les stats du match n°id

    path('tournament/', views.TournamentListView.as_view(), name='tournament-list'), # liste tous les tournaments
    path('tournament/<str:id>/', views.TournamentDetailView.as_view(), name='tournament-detail'), # affiche les detail du tournament n°id

    path('tournamentEvent/', views.TournamentEventListView.as_view(), name='tournamentEvent-list'), # liste tous les tournamentEvents
    path('tournamentEvent/<str:id>/', views.TournamentEventDetailView.as_view(), name='tournamentEvent-detail'), # affiche les detail du tournamentEvent n°id

    path('anecdote/', views.AnecdoteListView.as_view(), name='anecdote-list'), # liste tous les annecdotes
    path('anecdote/<str:id>/', views.AnecdoteDetailView.as_view(), name='anecdote-detail'), # affiche les detail du annecdote n°id

    path('city/', views.CityListView.as_view(), name='city-list'), # liste les "villes" (latitude, longitude) 
    path('city/<str:id>/', views.CityDetailView.as_view(), name='city-detail'), # liste la meteo heure par heure pour les 7 jours du la positon n°id
    path('city/<str:id>/moyenne/', views.CityMoyenneListView.as_view(), name='city-moyenne-detail'), # liste la meteo moyennée pour les 7 jours du la positon n°id

    path('meteo/images/<str:image_name>/', views.MeteoImageNameView.as_view(), name='meteo-image-name'), # renvois juste l'image "image_name".png qui se situe dans le dssier static/meteo/
                                                                                                         # seulement utilisé pour la view 'city-moyenne-detail'

    path('meteo/update/', views.MeteoUpdateView.as_view(), name='meteo-update'), # permet de faire une requete post de la latitude/longitude et renvois l'id de la "ville"
    #path('meteo/', views.MeteoListView.as_view(), name='meteo-list'), # Liste toutes les meteo
    path('meteo/<str:id>/', views.MeteoDetailView.as_view(), name='meteo-detail'), # affiche le detail de la meteo n°id
    path('meteo/<str:id>/image/', views.MeteoImageView.as_view(), name='meteo-image'), # renvois l'image de la meteo n°id en fonction de l'humitdité
]
