"""
module game. main exec file :)
"""
from exceptions import EnemyDown
from exceptions import GameOver
from models import Enemy
from models import Player


def play():
    """
    method play. :)
    """
    pl_name = input("Enter your name : ")
    player = Player(pl_name)
    level = 1
    enemy = Enemy(1)
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            level += 1
            player.score += 5
            enemy = Enemy(level)


def main():
    """
    method main. :)
    """
    try:
        play()
    except GameOver as g_o:
        print("GameOver")
        ffile = open('scores.txt', 'a')
        ffile.write(g_o.pl_name + ' - ' + g_o.pl_score + '\n')
        ffile.close
    except KeyboardInterrupt:
        pass
    finally:
        print("Good Bye!")


if __name__ == "__main__":
    main()
