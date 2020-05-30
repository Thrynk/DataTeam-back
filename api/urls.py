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
from rest_framework.routers import DefaultRouter

from . import views
from . import viewSets

routeur = DefaultRouter()
routeur.register('tennisPlayer', viewSets.TennisPlayerViewSet)
routeur.register('tennisPlayerStats', viewSets.TennisPlayerStatsViewSet)
routeur.register('Match', viewSets.MatchViewSet)
routeur.register('MatchStats', viewSets.MatchStatsViewSet)
routeur.register('Tournament', viewSets.TournamentViewSet)
routeur.register('TournamentEvent', viewSets.TournamentEventViewSet)

urlpatterns = [
    path('viewSets/', include(routeur.urls)),

    #path('tennisPlayers/', views.TennisPlayerList.as_view()),
    #path('tennisPlayers/<str:pk>', views.TennisPlayerDetail.as_view()),

    #path('tennisPlayerStats/', views.TennisPlayerStatsList.as_view()),
    #path('tennisPlayerStats/<str:pk>', views.TennisPlayerStatsDetail.as_view()),

    #path('tournaments/', views.TournamentList.as_view()),
    #path('tournaments/<str:pk>', views.TournamentDetail.as_view()),

    #path('tournamentEvents/', views.TournamentEventList.as_view()),
    #path('tournamentEvents/<str:pk>', views.TournamentEventDetail.as_view()),

    #path('matchs/', views.MatchList.as_view()),
    #path('matchs/<str:pk>', views.MatchDetail.as_view()),

    #path('matchStats/', views.MatchStatsList.as_view()),
    #path('matchStats/<str:pk>', views.MatchStatsDetail.as_view()),

]
