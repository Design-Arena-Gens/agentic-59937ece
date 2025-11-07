from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Player, TournamentRegistration
from tournaments.models import Tournament
from .forms import PlayerRegistrationForm

def home(request):
    tournaments = Tournament.objects.filter(is_active=True)[:3]
    return render(request, 'players/home.html', {'tournaments': tournaments})

def register_player(request):
    player_number = None
    tournaments = Tournament.objects.filter(is_active=True)

    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save()
            player_number = player.player_number

            # Register for tournament if selected
            tournament_id = request.POST.get('tournament')
            if tournament_id:
                try:
                    tournament = Tournament.objects.get(id=tournament_id)
                    TournamentRegistration.objects.create(
                        player=player,
                        tournament=tournament,
                        consent_given=request.POST.get('consent') == 'on'
                    )
                except Tournament.DoesNotExist:
                    pass

            return render(request, 'players/register.html', {
                'player_number': player_number,
                'tournaments': tournaments
            })
    else:
        form = PlayerRegistrationForm()

    return render(request, 'players/register.html', {
        'form': form,
        'tournaments': tournaments,
        'player_number': player_number
    })

def search_player(request):
    player = None
    player_number = request.GET.get('player_number')

    if player_number:
        try:
            player = Player.objects.get(player_number=player_number)
        except Player.DoesNotExist:
            player = None

    return render(request, 'players/search.html', {
        'player': player,
        'player_number': player_number
    })
