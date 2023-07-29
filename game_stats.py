class GameStats:

    def __init__(self, info):
        self.info = info
        self.reset_stats()

        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics Again"""
        self.ships_left = self.info.ship_limit
        self.score = 0
        self.level = 1
