from django.contrib import admin

from .models import ( 
    Match,
    MatchStats,
    TennisPlayer,
    TennisPlayerStats,
    Tournament,
    TournamentEvent
    )

# Register your models here.


admin.site.register(Match)
admin.site.register(MatchStats)
admin.site.register(TennisPlayer)
admin.site.register(TennisPlayerStats)
admin.site.register(Tournament)
admin.site.register(TournamentEvent)