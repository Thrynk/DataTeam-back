from django.contrib import admin
from . import models as my_models
# Register your models here.

admin.register(my_models.Match)
admin.register(my_models.MatchStats)
admin.register(my_models.TennisPlayer)
admin.register(my_models.TennisPlayerStats)
admin.register(my_models.Tournament)
admin.register(my_models.TournamentEvent)