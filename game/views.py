from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from game.models import Game, Player


def home(request):
    return render(request, 'game/home.html')


def login(request):
    return render(request, 'game/login.html')


def record_list(request):
    games = Game.objects.all()
    #User.objects.get(username=request.user.get_username())
    data = {
        'games': games,
    }
    return render(request, 'game/record_list.html', data)


def record_info(request, pk):
    record = Game.objects.get(pk=pk)
    data = {
        'record': record,
    }
    return render(request, 'game/record_info.html', data)


def atk(request, pk):
    dfs_choices = Player.objects.all()
    data = {
        'dfs_choices': dfs_choices
    }
    if request.method == 'POST':
        oppo = request.POST.get('oppo')
        game_choice = int(request.POST.get('rsp'))
        return redirect('game:atk_fin', atk.pk)
    return render(request, 'game/atk.html', data)


def atk_fin(request, pk):
    game = Game.objects.get(pk=pk)
    data = {
        'game': game
    }
    return render(request, 'game/atk_fin.html', data)


def dfs(request, pk):
    game = Game.objects.get(pk=pk)
    users = Player.objects.all()
    data = {
        'game': game
    }
    if request.method == 'POST':
        game.dfs = int(request.POST.get('rsp'))
        if game.atk == game.dfs:
            game.result = 3
            for user in users:
                if game.attacker == user.name or game.defender == user.name:
                    user.draw += 1
        elif game.atk - game.dfs == 1 or game.atk - game.dfs == -2:
            game.result = 1
            for user in users:
                if game.attacker == user.name:
                    user.win += 1
                    break
                if game.defender == user.name:
                    user.lose += 1
                    break
        else:
            game.result = 2
            for user in users:
                if game.attacker == user.name:
                    user.lose += 1
                    break
                if game.defender == user.name:
                    user.win += 1
                    break
        game.save()
        return redirect(reverse('dfs_fin', kwargs={'pk': game.pk}))
    return render(request, 'game/dfs.html', data)


def dfs_list(request, username):
    all_game = Game.objects.all()
    games = []
    for game in all_game:
        if game.defender == username and not game.result:
            games.append(game)

    data = {
        "games": games
    }
    return render(request, 'game/dfs_list.html', data)


def dfs_fin(request, pk):
    game = Game.objects.get(pk=pk)
    data = {
        "game": game
    }
    return render(request, 'game/dfs_fin.html', data)