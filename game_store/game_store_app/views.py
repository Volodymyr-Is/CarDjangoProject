from django.shortcuts import render, redirect, get_object_or_404
from game_store_app.models import *
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.decorators import login_required
from game_store_app.models import Comment
from game_store_app.forms import CommentForm, CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import auth
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def allGamesMain(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})

def allGamesShop(request):
    games = Game.objects.all()
    platforms = Platform.objects.all()
    genres = Genre.objects.all()
    developers = Developer.objects.all()
    tags = Tag.objects.all()
    return render(request, 'shop.html', {'games': games, 'platforms': platforms, 'genres': genres, 'developers': developers, 'tags': tags})

def gameById(request, gameId):
    game = get_object_or_404(Game, pk=gameId)
    comments = game.comments.all()
    form = CommentForm()
    return render(request, 'game.html', {'game': game, 'comments': comments, 'form': form})

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


def searchGame(request):
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


def filteredShop(request, data):
    try:
        platform = get_object_or_404(Platform, name=data)
        games = Game.objects.filter(platform=platform)
        filter = platform
    except Http404:
        try:
            genre = get_object_or_404(Genre, name=data)
            games = Game.objects.filter(genres=genre)
            filter = genre
        except Http404:
            try:
                developer = get_object_or_404(Developer, name=data)
                games = Game.objects.filter(developer=developer)
                filter = developer
            except Http404:
                try:
                    tag = get_object_or_404(Tag, name=data)
                    games = Game.objects.filter(tags=tag)
                    filter = tag
                except Http404:
                    games = []
                    filter = None

    platforms = Platform.objects.all()
    genres = Genre.objects.all()
    developers = Developer.objects.all()
    tags = Tag.objects.all()
    return render(request, 'shop.html', {'filter': filter, 'games': games, 'platforms': platforms, 'genres': genres, 'developers': developers, 'tags': tags})

def purchaseGame(request, gameId):
    game = get_object_or_404(Game, pk=gameId)
    return render(request, 'purchase.html', {'game': game})


@login_required
def addComment(request, gameId):
    logger.debug(f'AddComment called with gameId: {gameId}')
    game = get_object_or_404(Game, id=gameId)
    logger.debug(f'Game found: {game}')
    logger.debug(f'Current user: {request.user}')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        logger.debug(f'Form data: {request.POST}')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.game = game
            logger.debug(f'Comment before save: {comment}')
            try:
                comment.save()
                logger.debug('Comment saved successfully')
                return redirect('gameById', gameId=game.id)
            except Exception as e:
                logger.error(f'Error saving comment: {e}')
        else:
            logger.debug(f'Form errors: {form.errors}')
    else:
        form = CommentForm()
    
    return render(request, 'game.html', {'form': form, 'game': game})
# def addComment(request, gameId):
#     game = get_object_or_404(Game, id=gameId)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.game = game
#             comment.save()
#             return redirect('gameById', gameId=game.id)
#     else:
#         form = CommentForm()
#     return render(request, 'addComment.html', {'form': form})

@login_required
def editComment(request, gameId, commentId):
    game = get_object_or_404(Game, id=gameId)
    comment = get_object_or_404(Comment, id=commentId)
    if request.user != comment.user:
        return redirect('gameById', gameId=gameId)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('gameById', gameId=game.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/editComments.html', {'form': form})

@login_required
def deleteComment(request, gameId, commentId):
    comment = get_object_or_404(Comment, id=commentId)
    if request.user == comment.user:
        comment.delete()
    return redirect('gameById', gameId=gameId)



def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"Trying to authenticate user: {username}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("Authentication successful, logging in.")
                login(request, user)
                return redirect('home')
            else:
                print("Authentication failed, user is None.")
        else:
            print("Form is not valid.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')