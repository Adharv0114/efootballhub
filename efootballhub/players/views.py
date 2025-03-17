from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Player, Squad, Comparison
from .serializers import PlayerSerializer, SquadSerializer, ComparisonSerializer
from .forms import PlayerForm

# 1. Player Search API
@api_view(['GET'])
def search_players(request):
    query = request.GET.get('q', '')
    position = request.GET.get('position', '')
    playstyle = request.GET.get('playstyle', '')

    players = Player.objects.all()

    if query:
        players = players.filter(Q(name__icontains=query) | Q(club__icontains=query) | Q(nation__icontains=query))

    if position:
        players = players.filter(position=position)

    if playstyle:
        players = players.filter(playstyle__icontains=playstyle)

    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


# 2. Player Comparison API
@api_view(['GET'])
def compare_players(request):
    player1_id = request.GET.get('player1')
    player2_id = request.GET.get('player2')

    if not player1_id or not player2_id:
        return Response({"error": "Two player IDs are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        player1 = Player.objects.get(id=player1_id)
        player2 = Player.objects.get(id=player2_id)
    except Player.DoesNotExist:
        return Response({"error": "One or both players not found."}, status=status.HTTP_404_NOT_FOUND)

    comparison = Comparison(player1=player1, player2=player2)
    serializer = ComparisonSerializer(comparison)
    return Response(serializer.data)


# 3. Squad Management API
@api_view(['GET', 'POST'])
def squad_list_create(request):
    if request.method == 'GET':
        squads = Squad.objects.all()
        serializer = SquadSerializer(squads, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        squad_name = request.data.get('name')
        player_ids = request.data.get('players', [])

        squad = Squad.objects.create(name=squad_name)
        squad.players.set(Player.objects.filter(id__in=player_ids))

        serializer = SquadSerializer(squad)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


from django.shortcuts import render

def home(request):
    return render(request, 'players/home.html')

def create_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')  # Redirect to a list page after creation
    else:
        form = PlayerForm()
    
    return render(request, 'players/create_player.html', {'form': form})

def player_list(request):
    players = Player.objects.all()
    return render(request, 'players/player_list.html', {'players': players})

def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'players/player_detail.html', {'player': player})

def edit_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_detail', player_id=player.id)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'players/edit_player.html', {'form': form, 'player': player})

def delete_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == "POST":
        player.delete()
        return redirect('player_list')
    return render(request, 'players/delete_player.html', {'player': player})