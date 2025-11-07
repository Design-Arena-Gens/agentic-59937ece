from django.contrib import admin
from .models import Tournament, Team, TeamMember

class TeamInline(admin.TabularInline):
    model = Team
    extra = 0
    fields = ['name', 'mentor', 'logo']

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1
    autocomplete_fields = ['player']

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'is_active', 'created_date']
    list_filter = ['is_active', 'start_date', 'end_date']
    search_fields = ['name', 'description']
    inlines = [TeamInline]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'tournament', 'mentor', 'created_date']
    list_filter = ['tournament', 'created_date']
    search_fields = ['name', 'mentor', 'tournament__name']
    inlines = [TeamMemberInline]

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['player', 'team', 'assigned_date']
    list_filter = ['team__tournament', 'assigned_date']
    search_fields = ['player__name', 'team__name']
    autocomplete_fields = ['player']
