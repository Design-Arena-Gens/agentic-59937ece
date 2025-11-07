from django.contrib import admin
from .models import Player, TournamentRegistration
from datetime import date

class TournamentRegistrationInline(admin.TabularInline):
    model = TournamentRegistration
    extra = 0

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_number', 'name', 'age', 'gender', 'position', 'institution_name', 'registered_date']
    list_filter = ['gender', 'position', 'registered_date']
    search_fields = ['name', 'player_number', 'institution_name']
    readonly_fields = ['player_number', 'registered_date']
    inlines = [TournamentRegistrationInline]

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Age-based filtering
        if search_term:
            if 'under 14' in search_term.lower() or 'u14' in search_term.lower():
                today = date.today()
                max_year = today.year - 14
                queryset = queryset.filter(date_of_birth__year__gt=max_year)
            elif 'under 16' in search_term.lower() or 'u16' in search_term.lower():
                today = date.today()
                max_year = today.year - 16
                queryset = queryset.filter(date_of_birth__year__gt=max_year)
            elif 'under 17' in search_term.lower() or 'u17' in search_term.lower():
                today = date.today()
                max_year = today.year - 17
                queryset = queryset.filter(date_of_birth__year__gt=max_year)
            elif 'under 19' in search_term.lower() or 'u19' in search_term.lower():
                today = date.today()
                max_year = today.year - 19
                queryset = queryset.filter(date_of_birth__year__gt=max_year)
            elif 'girls' in search_term.lower():
                today = date.today()
                max_year = today.year - 18
                queryset = queryset.filter(gender='F', date_of_birth__year__gt=max_year)
            elif 'boys' in search_term.lower():
                today = date.today()
                max_year = today.year - 18
                queryset = queryset.filter(gender='M', date_of_birth__year__gt=max_year)
            elif 'women' in search_term.lower():
                today = date.today()
                max_year = today.year - 18
                queryset = queryset.filter(gender='F', date_of_birth__year__lte=max_year)
            elif 'men' in search_term.lower():
                today = date.today()
                max_year = today.year - 18
                queryset = queryset.filter(gender='M', date_of_birth__year__lte=max_year)

        return queryset, use_distinct

@admin.register(TournamentRegistration)
class TournamentRegistrationAdmin(admin.ModelAdmin):
    list_display = ['player', 'tournament', 'consent_given', 'registered_date']
    list_filter = ['tournament', 'consent_given', 'registered_date']
    search_fields = ['player__name', 'tournament__name']
