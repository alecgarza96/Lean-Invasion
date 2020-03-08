import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from lean import Lean


def run_game():
    #Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #make a ship, group of bullets, and group of lean
    ship = Ship(ai_settings, screen)
    bullets = Group()
    leans = Group()

    #create the fleet of lean
    gf.create_fleet(ai_settings, screen, ship, leans)

    #start the main loop for the game.
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, leans, bullets)
        gf.update_leans(ai_settings, leans)
        gf.update_screen(ai_settings, screen, ship, leans, bullets)
        

run_game()
