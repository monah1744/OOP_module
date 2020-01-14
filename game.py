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
            pass
            del enemy
            enemy = Enemy(level)


def main():
    try:
        play()
    except GameOver:
        print("GameOver")
    except KeyboardInterrupt:
        pass
    finally:
        print("Good Bye!")
        return 0


if __name__ == "__main__":
    main()
