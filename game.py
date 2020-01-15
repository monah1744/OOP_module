from exceptions import *
from models import Player
from models import Enemy
import settings


def play():
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
        return 0


if __name__ == "__main__":
    main()
