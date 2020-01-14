from random import randint
from exceptions import *


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return int(randint(1, 3))

    def decrease_lives(self):
        self.lives = self.lives-1
        print(f"Enemy lives - {self.lives}")
        if not self.lives:
            raise EnemyDown("Enemy Down")


class Player:
    def __init__(self, pl_name):
        self.pl_name = pl_name
        self.level = 1
        self.lives = 1
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        attack = int(attack)
        defense = int(defense)
        if attack == 1:
            if defense == 2:
                return 1
            if defense == 3:
                return -1
            if defense == 1:
                return 0

        if attack == 2:
            if defense == 3:
                return 1
            if defense == 1:
                return -1
            if defense == 2:
                return 0

        if attack == 3:
            if defense == 1:
                return 1
            if defense == 2:
                return -1
            if defense == 3:
                return 0

    def decrease_lives(self):
        self.lives = self.lives-1
        print(f"your lives - {self.lives}")
        if not self.lives:
            print(f"your score - {self.score}\n")
            raise GameOver("GameOver")

    def attack(self, enemy_obj):
        pl_choise = input("Your attack, Make your choise [1-3] : ")
        enemy_attack = Enemy.select_attack()
        if Player.fight(pl_choise, enemy_attack) > 0:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
        elif Player.fight(pl_choise, enemy_attack) < 0:
            print("You missed!")
        else:
            print("It's a draw!")

    def defence(self, enemy_obj):
        pl_choise = input("You defence, Make your choise [1-3] : ")
        enemy_attack = enemy_obj.select_attack()
        if Player.fight(enemy_attack, pl_choise) > 0:
            print("Enemy attacked successfully!")
            self.decrease_lives()
        elif Player.fight(enemy_attack, pl_choise) < 0:
            print("Enemy missed!")
        else:
            print("It's a draw!")
