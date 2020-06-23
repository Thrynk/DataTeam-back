from django.db import models
from datetime import datetime, timezone



# Create your models here.

# genereation de table sql a l'aide de model django
# exemple ici la table api2_tennisplayer sera crée avec tous ces champs 
class TennisPlayer(models.Model):

    #NATIONALITY_CHOICES = (
    #    ('S', 'Small'),
    #    ('M', 'Medium'),
    #    ('L', 'Large'),
    #    )

    name = models.CharField(max_length=15)
    firstname = models.CharField(max_length=15)
    nationality = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.firstname

class Tournament(models.Model):

    #SURFACE_CHOICES = (
    #    ('A', 'Acrylic'),
    #    ('B', 'Artificial clay'),
    #    ('C', 'Artificial grass'),
    #    ('D', 'Asphalt'),
    #    ('E', 'Carpet'),
    #    ('F', 'Clay'),
    #    ('G', 'Concrete'),
    #    ('H', 'Grass'),
    #    ('J', 'Other'),
    #    )

    name = models.CharField(max_length=15)
    surface = models.CharField(max_length=15)#, choices=SURFACE_CHOICES)
    date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name 

class TournamentEvent(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    season = models.CharField(max_length=15)
    date = models.DateField()

    def __str__(self):
        return self.tournament.name

class Match(models.Model):
    winner = models.ForeignKey(TennisPlayer, on_delete=models.CASCADE, related_name="winner")
    loser = models.ForeignKey(TennisPlayer, on_delete=models.CASCADE, related_name="loser")
    tournament_event = models.ForeignKey(TournamentEvent, on_delete=models.CASCADE)
    score = models.CharField(max_length=15)
    date = models.DateField()
    round = models.CharField(max_length=15)

    def __str__(self):
        return self.tournament_event.tournament.name

class MatchStats(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    winner_ace = models.IntegerField()
    winner_df = models.IntegerField()
    winner_serve_points = models.IntegerField()
    winner_1st_in = models.IntegerField()
    winner_1st_won = models.IntegerField()
    winner_2st_won = models.IntegerField()
    loser_ace = models.IntegerField()
    loser_df = models.IntegerField()
    loser_serve_points = models.IntegerField()
    loser_1st_in = models.IntegerField()
    loser_1st_won = models.IntegerField()
    loser_2st_won = models.IntegerField()

    def __str__(self):
        return self.match.tournament_event.tournament.name

class TennisPlayerStats(models.Model):

    player = models.OneToOneField(TennisPlayer, on_delete=models.CASCADE)
    matches_won=models.IntegerField()
    matches_lost=models.IntegerField()
    sets_won=models.IntegerField()
    sets_lost=models.IntegerField()
    aces = models.IntegerField()
    double_faults = models.IntegerField()
    serve_points = models.IntegerField()
    first_in = models.IntegerField()
    first_won = models.IntegerField()
    second_won = models.IntegerField()
    others_serve_points = models.IntegerField()
    others_1st_in = models.IntegerField()
    others_1st_won = models.IntegerField()
    others_2nd_won = models.IntegerField()
    others_breakpoints_saved = models.IntegerField()
    others_breakpoints_faced = models.IntegerField()

    def __str__(self):
        return self.player.name



class Anecdote(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class City(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    location_latitude = models.DecimalField(max_digits=15, decimal_places=8)
    location_longitude = models.DecimalField(max_digits=15, decimal_places=8)
    last_load=models.DateTimeField(default=datetime.now, blank=True)

class Meteo(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location_latitude = models.DecimalField(max_digits=15, decimal_places=8)
    location_longitude = models.DecimalField(max_digits=15, decimal_places=8)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2)
    date_time = models.CharField(max_length=50)

class Flag(models.Model):
    country_id = models.CharField(max_length=25)
    flag_png = models.CharField(max_length=25)

class Player_stats(models.Model):

    ace = models.IntegerField()
    df = models.IntegerField()
    serve_points = models.IntegerField()
    first_in = models.IntegerField()
    first_won = models.IntegerField()
    second_won = models.IntegerField()
    first_serve_success_percentage = models.DecimalField(max_digits=15, decimal_places=2)
    first_serve_won_percentage = models.DecimalField(max_digits=15, decimal_places=2)
    second_serve_won_percentage = models.DecimalField(max_digits=15, decimal_places=2)
    ace_percentage = models.DecimalField(max_digits=15, decimal_places=2)
    df_percentage = models.DecimalField(max_digits=15, decimal_places=2)
    firstname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    player_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'player_stats'

    def __str__(self):
        return self.player.name

class Player_stats_return(models.Model):

    opponent_ace = models.IntegerField()
    opponent_df = models.IntegerField()
    opponent_serve_points = models.IntegerField()
    opponent_first_in = models.IntegerField()
    opponent_first_won = models.IntegerField()
    opponent_second_won = models.IntegerField()
    winning_on_return_percentage = models.DecimalField(max_digits=15, decimal_places=2)
    winning_on_1st_serve_return_percentage = models.DecimalField(max_digits=15, decimal_places=2)
    winning_on_2nd_serve_return_percentage = models.DecimalField(max_digits=15, decimal_places=2)
    firstname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    player_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'player_stats_return'

class Prediction(models.Model):
    match= models.ForeignKey(Match, on_delete=models.CASCADE, related_name="match_id")
    player1 = models.ForeignKey(TennisPlayer, on_delete=models.CASCADE, related_name="player1_id")
    player2 = models.ForeignKey(TennisPlayer, on_delete=models.CASCADE, related_name="player2_id")
    player1_proba = models.DecimalField(max_digits=6, decimal_places=4)
    player2_proba = models.DecimalField(max_digits=6, decimal_places=4)

