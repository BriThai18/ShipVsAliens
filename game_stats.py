class GameStats():
    """Track statistics of the game"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start game in an inactive state
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
