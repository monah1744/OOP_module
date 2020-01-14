class GameOver(Exception):
    def __init__(self, message="GameOver"):
        super().__init__()
        self.message = message


class EnemyDown(Exception):
    def __init__(self, message="EnemyDown"):
        super().__init__()
        self.message = message


class Score():
    def __init__(self, message):
        super().__init__()
        self.message = message
