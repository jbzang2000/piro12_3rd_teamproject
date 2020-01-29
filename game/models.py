from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=20)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)


class Game(models.Model):
    attacker = models.CharField(max_length=20)
    atk = models.IntegerField()
    # 가위 0 바위 1 보 2
    defender = models.CharField(max_length=20)
    dfs = models.IntegerField(null=True)
    # 가위 0 바위 1 보 2
    result = models.IntegerField(null=True)
    # /(0 null 경기진행중:) /1:공격자가 승리 2:수비자가 승리 3:무승부

