import django_filters
from .models import *

class TennisPlayerFilter(django_filters.FilterSet):
    class Meta:
        model = TennisPlayer
        fields = '__all__'