from django.db import models

# Create your models here.

class TennisPlayer(models.Model):
    name = models.CharField(max_length=15)
    firstname = models.CharField(max_length=15)
    nationality = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=15)
    surface = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    date = models.DateField()

    def __str__(self):
        return self.name

class TournamentEvent(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    season = models.CharField(max_length=15)
    date = models.DateField()

class Match(models.Model):
    winner = models.ForeignKey(TennisPlayer, on_delete=models.CASCADE, related_name="winner")
    loser = models.ForeignKey(TennisPlayer, on_delete=models.CASCADE, related_name="loser")
    tournament_event = models.ForeignKey(TournamentEvent, on_delete=models.CASCADE)
    score = models.CharField(max_length=15)
    date = models.DateField()
    round = models.CharField(max_length=15)

class MatchStats(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    winner_ace = models.IntegerField()
    winner_df = models.IntegerField()
    winner_serve_points = models.IntegerField()
    winner_1st_in = models.IntegerField()
    winner_1st_won = models.IntegerField()
    winner_2st_won = models.IntegerField()
    loser_df = models.IntegerField()
    loser_serve_points = models.IntegerField()
    loser_1st_in = models.IntegerField()
    loser_1st_won = models.IntegerField()
    loser_2st_won = models.IntegerField()

    def __str__(self):
        return self.match

class TennisPlayerStats(models.Model):
    player = models.ForeignKey(TennisPlayer, on_delete=models.CASCADE)
    matches_won=models.IntegerField()
    matches_lost=models.IntegerField()

    def __str__(self):
        return self.player


