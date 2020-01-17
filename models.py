"""
module models. describe models Enemy and Player :)
"""


from random import randint
from exceptions import EnemyDown
from exceptions import GameOver
from settings import LIVES


class Enemy:
    """
    Class Enemy. describe model Enemy:)
    """

    def __init__(self, level):
        """
        init method :)
        """
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """
        method atack. random :)
        """
        return int(randint(1, 3))

    def decrease_lives(self):
        """
        method decrease_lives. :)
        """
        self.lives = self.lives-1
        print(f"Enemy lives - {self.lives}")
        if not self.lives:
            raise EnemyDown()


class Player:
    """
    Class Player. describe model Player:)
    """

    def __init__(self, pl_name):
        """
        method init :)
        """
        self.pl_name = pl_name
        self.lives = LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        """
        method fight :)
        """
        win = [(1, 2), (2, 3), (3, 1)]
        lose = [(1, 3), (2, 1), (3, 2)]
        draw = [(1, 1), (2, 2), (3, 3)]
        fight_case = (int(attack), int(defense))
        if fight_case in win:
            return 1
        if fight_case in lose:
            return -1
        if fight_case in draw:
            return 0
        return 0

    def decrease_lives(self):
        """
        method decrease_lives :)
        """
        self.lives = self.lives-1
        print(f"your lives - {self.lives}")
        if not self.lives:
            print(f"your score - {self.score}\n")
            raise GameOver(self)

    @staticmethod
    def attack(enemy_obj):
        """
        method atack :)
        """
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
        """
        method defence :)
        """
        pl_choise = input("You defence, Make your choise [1-3] : ")
        enemy_attack = enemy_obj.select_attack()
        if Player.fight(enemy_attack, pl_choise) > 0:
            print("Enemy attacked successfully!")
            self.decrease_lives()
        elif Player.fight(enemy_attack, pl_choise) < 0:
            print("Enemy missed!")
        else:
            print("It's a draw!")
