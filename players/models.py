from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import random

def generate_player_number():
    return random.randint(1000, 9999)

class Player(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    POSITION_CHOICES = [
        ('GS', 'Goal Shooter'),
        ('GA', 'Goal Attack'),
        ('WA', 'Wing Attack'),
        ('C', 'Centre'),
        ('WD', 'Wing Defence'),
        ('GD', 'Goal Defence'),
        ('GK', 'Goal Keeper'),
    ]

    player_number = models.IntegerField(unique=True, default=generate_player_number, editable=False)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    photo = models.ImageField(upload_to='player_photos/', default='player_photos/default.jpg', blank=True)
    institution_name = models.CharField(max_length=300)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.player_number}"

    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    class Meta:
        ordering = ['-registered_date']

class TournamentRegistration(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='tournament_registrations')
    tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.CASCADE, related_name='player_registrations')
    registered_date = models.DateTimeField(auto_now_add=True)
    consent_given = models.BooleanField(default=True)

    class Meta:
        unique_together = ['player', 'tournament']
        ordering = ['-registered_date']

    def __str__(self):
        return f"{self.player.name} - {self.tournament.name}"
