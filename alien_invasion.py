import sys
import pygame
import game_functions as gf 

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pygame.sprite import Group

def run_game():
    #Initalize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make the play button
    play_button = Button(ai_settings, screen, "Play")

    #Create instance to store statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Make a ship
    ship = Ship(ai_settings, screen)

    #Group to store bullets and alien
    bullets = Group()
    aliens = Group()

    #Create fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Background
    bg_color = (230, 230, 230)

    #Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
