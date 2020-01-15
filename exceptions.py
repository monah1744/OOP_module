class GameOver(Exception):
    def __init__(self, message, some_obj):
        super().__init__()
        self.message = message
        self.pl_name = some_obj.pl_name
        self.pl_score = some_obj.score


class EnemyDown(Exception):
    def __init__(self, message="EnemyDown"):
        super().__init__()
        self.message = message


class Score():
    def __init__(self, message):
        super().__init__()
        self.message = message
