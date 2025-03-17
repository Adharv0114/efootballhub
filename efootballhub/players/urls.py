from django.urls import path
from .views import search_players, compare_players, squad_list_create, create_player, player_list, player_detail, edit_player, delete_player
from django.shortcuts import render

urlpatterns = [
    path('players/search/', search_players, name='search_players'),
    path('players/compare/', compare_players, name='compare_players'),
    path('squads/', squad_list_create, name='squad_list_create'),
    path('search/', lambda request: render(request, 'players/search.html'), name='player_search_page'),
    path('compare/', lambda request: render(request, 'players/compare.html'), name='compare_page'),
    path('squad/', lambda request: render(request, 'players/squad.html'), name='squad_page'),
    path('create/', lambda request: render(request, 'players/create_player.html'), name='create_page'),
    path('players/create/', create_player, name='create_player'),
    path('players/', player_list, name='player_list'),
    path('players/<int:player_id>/', player_detail, name='player_detail'),
    path('players/<int:player_id>/edit/', edit_player, name='edit_player'),
    path('players/<int:player_id>/delete/', delete_player, name='delete_player'),
    path('players/<int:player_id>/delete/', delete_player, name='delete_player'),
]
