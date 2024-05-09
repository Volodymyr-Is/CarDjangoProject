from django.shortcuts import render, redirect, get_object_or_404
from game_store_app.models import *
from django.http import Http404
from django.urls import reverse
from django.core.exceptions import MultipleObjectsReturned

# Create your views here.
def allGamesMain(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})

def allGamesShop(request):
    games = Game.objects.all()
    return render(request, 'shop.html', {'games': games})

def gameById(request, gameId):
    game = get_object_or_404(Game, pk=gameId)
    return render(request, 'game.html', {'game': game})

def gamesByData(request, data):
    try:
        platform = get_object_or_404(Platform, name=data)
        games = Game.objects.filter(platform=platform)
        data_to_use = platform
    except Http404:
        try:
            genre = get_object_or_404(Genre, name=data)
            games = Game.objects.filter(genres=genre)
            data_to_use = genre
        except Http404:
            try:
                developer = get_object_or_404(Developer, name=data)
                games = Game.objects.filter(developer=developer)
                data_to_use = developer
            except Http404:
                try:
                    tag = get_object_or_404(Tag, name=data)
                    games = Game.objects.filter(tags=tag)
                    data_to_use = tag
                except Http404:
                    games = []
                    data_to_use = None
    
    return render(request, 'findBy_page.html', {'data': data_to_use, 'games': games})


def findGame(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        if search_query.strip() != "":
            try:
                game = Game.objects.get(title__icontains=search_query)
                return redirect(reverse('gameById', args=[game.pk]))
            except Game.DoesNotExist:
                raise Http404("Game does not exist")
            except MultipleObjectsReturned:
                raise Http404("Multiple games match the search query")
        else:
            pass
    return redirect('home')


# def findGame(request):
#     if request.method == 'POST':
#         search_query = request.POST.get('search_query', '')
#         if search_query.strip() != "":
#             try:
#                 game = Game.objects.get(title__icontains=search_query)
#                 return redirect(reverse('gameById', args=[game.pk]))
#             except Game.DoesNotExist:
#                 raise Http404("Game does not exist")
#             except MultipleObjectsReturned:
#                 raise Http404("Multiple games match the search query")
#             try:
#                 platform = get_object_or_404(Platform, name=data)
#                 games = Game.objects.filter(platform=platform)
#                 data_to_use = platform
#             except Http404:
#                 try:
#                     genre = get_object_or_404(Genre, name=data)
#                     games = Game.objects.filter(genres=genre)
#                     data_to_use = genre
#                 except Http404:
#                     try:
#                         developer = get_object_or_404(Developer, name=data)
#                         games = Game.objects.filter(developer=developer)
#                         data_to_use = developer
#                     except Http404:
#                         try:
#                             tag = get_object_or_404(Tag, name=data)
#                             games = Game.objects.filter(tags=tag)
#                             data_to_use = tag
#                         except Http404:
#                             games = []
#                             data_to_use = None
            
#             return render(request, 'findBy_page.html', {'data': data_to_use, 'games': games})
#         else:
#             pass
#     return redirect('home')