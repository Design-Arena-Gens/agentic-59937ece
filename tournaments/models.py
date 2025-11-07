from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']

class Team(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    mentor = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.tournament.name}"

    class Meta:
        ordering = ['name']

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE, related_name='team_memberships')
    assigned_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['team', 'player']
        ordering = ['-assigned_date']

    def __str__(self):
        return f"{self.player.name} - {self.team.name}"
