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

from . import views

urlpatterns = [
    path('overview', views.apiOverview),

    path('tennisPlayers/', views.TennisPlayerList.as_view()),
    path('tennisPlayers/<str:pk>', views.TennisPlayerDetail.as_view()),

    path('tennisPlayerStats/', views.TennisPlayerStatsList.as_view()),
    path('tennisPlayerStats/<str:pk>', views.TennisPlayerStatsDetail.as_view()),

    path('Tournaments/', views.TournamentList.as_view()),
    path('Tournaments/<str:pk>', views.TournamentDetail.as_view()),

    path('TournamentEvents/', views.TournamentEventList.as_view()),
    path('TournamentEvents/<str:pk>', views.TournamentEventDetail.as_view()),

    path('Matchs/', views.MatchList.as_view()),
    path('Matchs/<str:pk>', views.MatchDetail.as_view()),

    path('MatchStats/', views.MatchStatsList.as_view()),
    path('MatchStats/<str:pk>', views.MatchStatsDetail.as_view()),

]
