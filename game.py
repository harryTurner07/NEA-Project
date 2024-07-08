# Example file showing a basic pygame "game loop"
import pygame
import random

# Unused stuff
"""
# An attempt at doing a sprint mechanic, can very much be improved so... GL future me :)
    if pygame.K_LSHIFT:
        circle_x_vel += 4
    else:
        circle_x_vel = 1
circle_sprint_modifier = 4  # This gets added onto the velocity of the circle, so make it one lower than desired
"""



# pygame setup
pygame.init()
pygame.display.set_caption("Bullet Hell Idea for NEA WIP")
WIDTH = 1280
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
running = True
FPS = 60
PUREWHITE = (255,255,255)



# Bullet Stuff    
PURERED = (255,0,0)
bullet_x = random.randint(0,WIDTH)
bullet_y = random.randint(0,HEIGHT)
bullet_radius = 5
bullet_vel = 3

# Circle Stuff
circle_x = 100
circle_y = 100
circle_radius = 10
circle_x_vel = 5

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if (circle_x == bullet_x) or (circle_y == bullet_y):
        pygame.QUIT

    # fill the screen with a color to wipe away anything from last frame
    SCREEN.fill("purple")

    # RENDER YOUR GAME HERE
    circle = pygame.draw.circle(SCREEN,center=(circle_x,circle_y),color=PUREWHITE,radius=(circle_radius))

    bullet = pygame.draw.circle(SCREEN,center=(bullet_x,bullet_y),color=PURERED,radius=(circle_radius))
    bullet_x += bullet_vel

    # collision with the borders of window and looping FOR CIRCLE / CHARACTER
    # For the X coordinates
    if circle_x < 0:
        circle_x = WIDTH
    if circle_x > WIDTH:
        circle_x = 0
    # For the Y coordinates
    if circle_y < 0:
        circle_y = HEIGHT
    if circle_y > HEIGHT:
        circle_y = 0

    # Collision for Bullets
    # For the X coordinates
    if bullet_x < 0:
        bullet_x = WIDTH
    if bullet_x > WIDTH:
        bullet_x = 0
    # For the Y coordinates
    if bullet_y < 0:
        bullet_y = HEIGHT
    if bullet_y > HEIGHT:
        bullet_y = 0

    # Key press things

    # stores keys pressed
    keys = pygame.key.get_pressed()

    # if left arrow key is pressed 
    if keys[pygame.K_LEFT]: 
        # decrement in x co-ordinate 
        circle_x -= circle_x_vel
    # if left arrow key is pressed 
    if keys[pygame.K_RIGHT]: 
        # increment in x co-ordinate 
        circle_x += circle_x_vel
    # if left arrow key is pressed    
    if keys[pygame.K_UP]: 
        # decrement in y co-ordinate 
        circle_y -= circle_x_vel
    # if left arrow key is pressed    
    if keys[pygame.K_DOWN]: 
        # increment in y co-ordinate 
        circle_y += circle_x_vel
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    CLOCK.tick(FPS)  # limits FPS to 60

pygame.quit()