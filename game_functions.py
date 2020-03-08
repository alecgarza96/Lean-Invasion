import sys
import pygame
from bullet import Bullet
from lean import Lean

def check_keydown_events(event,ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    #create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """Respond to key releasese."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
               
def update_screen(ai_settings, screen, ship, leans, bullets):
    """Update iages on the screen and flip to the new screen."""
    #redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    leans.draw(screen)

    #make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, leans, bullets):
    """Update position of bullets and get rid of old bullets."""
    #update bullet positions
    bullets.update()
    #get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
             bullets.remove(bullet)
             
    check_bullet_lean_collisions(ai_settings, screen, ship, leans, bullets)

def check_bullet_lean_collisions(ai_settings, screen, ship, leans, bullets):
    """Respond to bullet-lean collisions."""
    #remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, leans, True, True)
    
def get_number_leans_x(ai_settings, lean_width):
    """Determine th enumber of leans that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * lean_width
    number_leans_x = int(available_space_x/(2*lean_width))
    return number_leans_x

def get_number_rows(ai_settings, ship_height, lean_height):
    """Determine the number of rows of lean that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (3* lean_height)-ship_height)
    number_rows = int(available_space_y / (2*lean_height))
    return number_rows

def create_lean(ai_settings, screen, leans, lean_number, row_number):
    """Create lean and place it in a row"""
    lean = Lean(ai_settings, screen)
    lean_width = lean.rect.width
    lean.x = lean_width + 2 * lean_width * lean_number
    lean.rect.x = lean.x
    lean.rect.y = lean.rect.height + 2 * lean.rect.height * row_number
    leans.add(lean)

def create_fleet(ai_settings, screen, ship, leans):
    """Create a full fleet of lean cups."""
    #create an alien and find the number of aliens in a row
    #spacing between each alien is equal to one alien width
    lean = Lean(ai_settings, screen)
    number_leans_x = get_number_leans_x(ai_settings, lean.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, lean.rect.height)

    #create the first row of aliens
    for row_number in range(number_rows):
        for lean_number in range(number_leans_x):
            create_lean(ai_settings, screen, leans, lean_number, row_number)

def update_leans(leans):
    """update the positions of lean in the fleet"""
    leans.update()

def check_fleet_edges(ai_settings, leans):
    """Respond appropriately if any leans have reached an edge."""
    for lean in leans.sprites():
        if lean.check_edges():
            change_fleet_direction(ai_settings, leans)
            break

def change_fleet_direction (ai_settings, leans):
    """Drop the entire fleet and change the fleets direction."""
    for lean in leans.sprites():
        lean.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_leans(ai_settings, leans):
    """
Check if the fleet is at an edge,
and then update the positions of all lean in the fleet
"""
    check_fleet_edges(ai_settings, leans)
    leans.update()
