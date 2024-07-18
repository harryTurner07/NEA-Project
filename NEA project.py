# Example file showing a basic pygame "game loop"
"""
This template was taken from my computer science teacher
Some code will most likely be taken from the "game py" file
or will be taken from websites like StackOverflow, W3Schools and other sites that I'll either add here
or will say when it appears
"""
import pygame
import random

# pygame setup
def main():
    pygame.init()
    pygame.display.set_caption("NEA Project")
    WIDTH = 1280
    HEIGHT = 720
    FPS = 60
    SCREEN= pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    running = True

    # Player things
    DEFAULT_PLAYER_SIZE = (64,64)
    #^^^ The image resoultion used is a 64,64 image.
    player_x = 100
    player_y = 100
    DEFAULT_PLAYER_POS = (player_x,player_y)
    player_vel = 5
    angle = 1

    # Enemy 1 (shooter) things
    enemy_x = random.randint(0, WIDTH)
    enemy_y = random.randint(0, HEIGHT)
    enemy_vel = 3
    start_time = 0

    # Test for making player as a class...
    # IT WORKS !!!!! <---- This will backfire in a few attempts
    class Player:
        def __init__(self, player_x_pos, player_y_pos, player_velo,image):
            self.player_x_pos = player_x
            self.player_y_pos = player_y
            self.player_velo = player_vel
            self.image = image
        def _playerblit_(self):
            SCREEN.blit(self.image, (player_x, player_y))

    # Hopefully an enemy class
    class Enemy:
        def __init__(self, enemy_x, enemy_y, enemy_vel, image):
            self.enemy_x_pos = enemy_x
            self.enemy_y_pos = enemy_y
            self.enemy_velo = enemy_vel
            self.image = image
        def _enemyblit_(self):
            SCREEN.blit(self.image, (enemy_x, enemy_y))

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                start_time = pygame.time.get_ticks()

        # fill the screen with a color to wipe away anything from last frame
        SCREEN.fill("orange")

        """ RENDER YOUR GAME HERE """
        #player = pygame.draw.circle(SCREEN,center=(player_x,player_y),color=(255,255,255),radius=(player_radius))
        # Old code for rendering the player as a drawn object
        #player = pygame.image.load("Test-Image.png")
        # Loads the player and enemy
        player = Player(player_x, player_y, player_vel, (pygame.image.load("Test-Image.png")))

        enemy = Enemy((random.randint(0,WIDTH)), (random.randint(0,HEIGHT)), enemy_vel, (pygame.image.load("Test-Enemy.png")))
        enemy._enemyblit_()
        
        # Should hopefully always update the position of the mouse
        mouse_pos = pygame.mouse.get_pos()

        """
        # Borders but for the enemy class(s)
        # X coordinates
        if enemy_x < 1:
            enemy_x = 10
        if enemy_x > (WIDTH - 1):
            enemy_x = (WIDTH - 9)
        # Y coordinates
        if enemy_y < 1:
            enemy_y = 10
        if enemy_y > (HEIGHT - 1):
            enemy_y = (HEIGHT - 9)
        """

        # Code stolen from game py
        # Enemy loops around
        # For the X coordinates
        if enemy_x < 0:
            enemy_x = WIDTH
        if enemy_x > WIDTH:
            enemy_x = 0
        # For the Y coordinates
        if enemy_y < 0:
            enemy_y = HEIGHT
        if enemy_y > HEIGHT:
            enemy_y = 0

        # Scaling the image to the desired size (should already be at 64x64, this is just in case)
        #player = pygame.transform.scale(player, DEFAULT_PLAYER_SIZE)
        # ROTATION
        #player = pygame.transform.rotate(player, angle=(angle))
        #angle += 1
        # Updating
        #SCREEN.blit(player, (player_x, player_y))

        # Updates the positions of the player and enemy(s)
        player._playerblit_()

        # Enemy movement, selects a random number and depending on the range that the number
        # goes into, for a range of 10 (not too sure how it works, but it does)
        # then it increases / decreases the x or y axis by the enemy's velocity
        rand_num = random.randint(1,20)
        if 1 <= rand_num <= 5:
            for i in range(5):
                enemy_x += enemy_vel
                enemy_y -= enemy_vel
        if 6 <= rand_num <= 10:
            for i in range(5):
                enemy_y -= enemy_vel
                enemy_x -= enemy_vel
        if 11 <= rand_num <= 15:
            for i in range(5):
                enemy_x -= enemy_vel
                enemy_y += enemy_vel
        if 16 <= rand_num <= 20:
            for i in range(5):
                enemy_y += enemy_vel
                enemy_x += enemy_vel

        # Stores the keys pressed
        keys = pygame.key.get_pressed()

        # This was taken from game.py - Don't think the code was taken from anywhere
        # !!! The "and" sections were taken from GeeksForGeeks, see the write-up

        # if a (left) key is pressed 
        if keys[pygame.K_a] and player_x> 0: 
            # decrement in x co-ordinate 
            player_x -= player_vel
        # if d (right) key is pressed 
        if keys[pygame.K_d] and player_x < WIDTH - 64: 
            # increment in x co-ordinate 
            player_x += player_vel
        # if w (up) key is pressed    
        if keys[pygame.K_w] and player_y> 0: 
            # decrement in y co-ordinate 
            player_y -= player_vel
        # if s (down) key is pressed    
        if keys[pygame.K_s] and player_y < HEIGHT - 64: 
            # increment in y co-ordinate 
            player_y += player_vel

        # Quit Key  
        if keys[pygame.K_q]:
            running = False

        # flip() the display to put your work on screen
        pygame.display.flip()

        CLOCK.tick(FPS)  # limits FPS to 60

    pygame.quit()

if __name__ == '__main__':
    main()