from django.shortcuts import render, redirect
from django.urls import reverse
from game.models import Game, Player


def home(request):
    return render(request, 'game/home.html')


def login(request):
    return render(request, 'game/login.html')


def record_list(request):
    allgames = Game.objects.all()
    player = Player.objects.get(name=request.user.get_username())
    games = []
    for game in allgames:
        if game.attacker == request.user.get_username() or game.defender == request.user.get_username():
            games.append(game)
        # User.objects.get(username=request.user.get_username())
    data = {
        'games': games,
        'player': player,
    }
    return render(request, 'game/record_list.html', data)


def record_info(request, pk):
    record = Game.objects.get(pk=pk)
    data = {
        'record': record,
    }
    return render(request, 'game/record_info.html', data)


def atk(request):
    dfs_choices = Player.objects.all()
    data = {
        'dfs_choices': dfs_choices,
        'user_name': request.user.get_username()
    }
    if request.method == 'POST':
        oppo = request.POST.get('oppo')
        game_choice = int(request.POST.get('rsp'))
        user = request.user.get_username()
        Game.objects.create(attacker=user, atk=game_choice, defender=Player.objects.get(pk=oppo).name)
        return redirect(reverse('game:atk_fin'))
    return render(request, 'game/atk.html', data)


def sign(request):
    try:
        Player.objects.get(name=request.user.get_username())

    except:
        Player.objects.create(name=request.user.get_username())

    return redirect(reverse('game:home'))


def atk_fin(request):
    return render(request, 'game/atk_fin.html')


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
                    user.save()
        elif game.atk - game.dfs == 1 or game.atk - game.dfs == -2:
            game.result = 1
            for user in users:
                if game.attacker == user.name:
                    user.win += 1
                    user.save()
                if game.defender == user.name:
                    user.lose += 1
                    user.save()

        else:
            game.result = 2
            for user in users:
                if game.attacker == user.name:
                    user.lose += 1
                    user.save()

                if game.defender == user.name:
                    user.win += 1
                    user.save()

        game.save()
        return redirect(reverse('game:dfs_fin', kwargs={'pk': game.pk}))
    return render(request, 'game/dfs.html', data)


def dfs_list(request):
    all_game = Game.objects.all()
    games = []
    for game in all_game:
        if game.defender == request.user.get_username() and not game.result:
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
