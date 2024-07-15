# Example file showing a basic pygame "game loop"
"""
This template was taken from my computer science teacher
Some code will most likely be taken from the "game.py" file
or will be taken from websites like StackOverflow, W3Schools and other sites that I'll either add here
or will say when it appears
"""
import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("NEA Project")
WIDTH = 1280
HEIGHT = 720
FPS = 60
SCREEN= pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
DEFAULT_PLAYER_SIZE = (64,64)
#^^^ The image resoultion used is a 64,64 image.
running = True
player_x = 100
player_y = 100
player_radius = 5
player_vel = 5

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    SCREEN.fill("orange")

    """ RENDER YOUR GAME HERE """
    #player = pygame.draw.circle(SCREEN,center=(player_x,player_y),color=(255,255,255),radius=(player_radius))
    # Old code for rendering the player as a drawn object
    player = pygame.image.load("Test-Image.png")
    SCREEN.blit(player,(player_x, player_y))

    # Should hopefully always update the position of the mouse
    mouse_pos = pygame.mouse.get_pos()

    # Borders - Temporary, but works at the moment
    # Idea is that the player gets "teleported" back when they reach that position
    # X coordinates
    if player_x < 1:
        player_x = 10
    if player_x > (WIDTH - 1):
        player_x = (WIDTH - 9)
    # Y coordinates
    if player_y < 1:
        player_y = 10
    if player_y > (HEIGHT - 1):
        player_y = (HEIGHT - 9)

    # Stores the keys pressed
    keys = pygame.key.get_pressed()

    # This was taken from game.py - Don't think the code was taken from anywhere

    # if a (left) key is pressed 
    if keys[pygame.K_a]: 
        # decrement in x co-ordinate 
        player_x -= player_vel
    # if d (right) key is pressed 
    if keys[pygame.K_d]: 
        # increment in x co-ordinate 
        player_x += player_vel
    # if w (up) key is pressed    
    if keys[pygame.K_w]: 
        # decrement in y co-ordinate 
        player_y -= player_vel
    # if s (down) key is pressed    
    if keys[pygame.K_s]: 
        # increment in y co-ordinate 
        player_y += player_vel

    # flip() the display to put your work on screen
    pygame.display.flip()

    CLOCK.tick(FPS)  # limits FPS to 60

pygame.quit()