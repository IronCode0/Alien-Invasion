import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    info = Settings()
    screen = pygame.display.set_mode((info.screen_width, info.screen_height))
    pygame.display.set_caption("Alien Invasion 2.0")

    play_button = Button(info, screen, "Let Start")
    
    stats = GameStats(info)
    sb = Scoreboard(info, screen, stats)
    
    bg_color = (230, 230, 230)

    ship = Ship(info, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(info, screen, ship, aliens)

    while True:
        gf.check_events(info, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(info, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(info, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(info, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
