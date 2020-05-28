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


from rest_framework import routers

from . import v1
from . import v2


router = routers.DefaultRouter()
#router.register('users_list', viewsSerializers.usersListViewSet)

urlpatterns = [
    path('routeur/', include(router.urls), name='api.router'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'), name='api.rest_framework'),

    path('v1/', include('api.v1.urls'), name='api.v1'),
    path('v2/', include('api.v2.urls'), name='api.v2'),

    #path('', include(router.urls), name='api.router'),
]
