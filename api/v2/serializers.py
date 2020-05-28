from rest_framework import serializers

#from .models import Hero
from django.contrib.auth.models import User

#class UserSerializer(serializers.HyperlinkedModelSerializer):
#class UserSerializer(serializers.Serializer):
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']