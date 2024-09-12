# Example file showing a basic pygame "game loop"

# Will I be able to put this into a playable state by the time this has to be presented October - November - December time?
# Yes
# Will my mental health be stable?
# Absolutely not

# Im planning on doing more stuff when college has actually started, but for now it's barely "eh"..
# Upon saying that, when the file is executed, all images stay at the top and don't refresh
# May God save us all

"""
This template was taken from my computer science teacher
Some code will most likely be taken from the "game py" file
or will be taken from websites like StackOverflow, W3Schools and other sites that I'll either add here
or will say when it appears
"""
import pygame
import random
import math

# Test for push

# Second test for push

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
    background_img = pygame.image.load("space-background.png")

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
    enemy_amount = []

    # Midpoint stuff
    total_x = player_x + enemy_y
    midpoint_x = (total_x // 2)
    total_y = player_y + enemy_y
    midpoint_y = (total_y // 2)
    midpoint_y2 = midpoint_y - random.randint(0,75)
    player_x2 = player_x - 100
    player_y2 = player_y - 100

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
    # Currently unused
    class Enemy:
        def __init__(self, enemy_x, enemy_y, enemy_vel, image):
            self.enemy_x_pos = enemy_x
            self.enemy_y_pos = enemy_y
            self.enemy_velo = enemy_vel
            self.image = image
        def _enemyblit_(self):
            SCREEN.blit(self.image, (self.enemy_x_pos, self.enemy_y_pos))
        # Code to make the enemy move towards the player - From StackOverflow
        def move_towards_player(self, Player):
            # Find direction vector (dx, dy) between enemy and player
            dx, dy = Player.player_x_pos - self.enemy_x_pos, Player.player_y_pos - self.enemy_y_pos
            # Returns the hypotenuse; the long side, so it's a direct line to the player
            # Not entirely what I want to do, but if it works, then I'll keep it that way unless otherwise
            dist = math.hypot(dx, dy)
            dx, dy = dx / dist, dy / dist # Normalise
            # Move along this normalised vector towards the player at current speed
            self.enemy_x_pos += dx * self.enemy_velo
            self.enemy_y_pos += dy * self.enemy_velo
            print("AAAAAAAAAAAAAAAAAA")


    def enemy_xory_value_moving(enemy_x, enemy_y, player_x, player_y, enemy_vel):
        if enemy_x < player_x:
            while enemy_x < (player_x + random.randint(10,100)):
                enemy_x += enemy_vel
        elif enemy_y < enemy_y:
            while enemy_y < (player_y + random.randint(10,100)):
                enemy_y += enemy_vel

    """
        While running things
    """
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                start_time = pygame.time.get_ticks()

        # fill the screen with a color to wipe away anything from last frame
        #SCREEN.fill("orange")
        # set the background from the position 0,0
        SCREEN.blit(background_img, (0,0))

        """ RENDER YOUR GAME HERE """
        #player = pygame.draw.circle(SCREEN,center=(player_x,player_y),color=(255,255,255),radius=(player_radius))
        # Old code for rendering the player as a drawn object
        #player = pygame.image.load("Test-Image.png")
        # Loads the player and enemy
        player = Player(player_x, player_y, player_vel, (pygame.image.load("Test-Image.png")))
        #enemy = Enemy((enemy_x + random.randint(10, 100)), (enemy_y + random.randint(10,100)), enemy_vel, (pygame.image.load("Test-Enemy.png")))
        #enemy = pygame.draw.circle(SCREEN, center=(enemy_x, enemy_y), color=(255,255,255), radius=0)
        #enemy = pygame.image.load("Test-Enemy.png")
        enemy = Enemy(enemy_x, enemy_y, enemy_vel, (pygame.image.load("Test-Enemy.png")))
        # play around with enemy.surface <- look on pygame
        enemy.move_towards_player(player)
        enemy._enemyblit_()
        
        # Another attempt to spawn in multiple enemies
        


        # Supposed to spawn in multiple enemies
        """
        while len(enemy_amount) != 5:
            enemy = pygame.draw.circle(SCREEN, center=(enemy_x, enemy_y), color=(255,255,255), radius=0)
            enemy = pygame.image.load("Test-Enemy.png")
            enemy_amount.append(enemy)
        """

        # Code for moving the enemey around, I think it works but the only thing it does is just mirror the movements

        """
        # If and while the enemy_x value is lower than the player_x value, increase it
        if enemy_x < player_x2:
            while enemy_x < player_x2:
                enemy_x += enemy_vel
                SCREEN.blit(enemy, (enemy_x, enemy_y))
        
        if enemy_y < player_y2:
            while enemy_y < player_y2:
                enemy_y += enemy_vel
                SCREEN.blit(enemy, (enemy_x, enemy_y))
        
        if enemy_x > player_x2:
            while enemy_x > player_x2:
                enemy_x -= enemy_vel
                SCREEN.blit(enemy, (enemy_x, enemy_y))

        if enemy_y > player_y2:
            while enemy_y > player_y2:
                enemy_y -= enemy_vel
                SCREEN.blit(enemy, (enemy_x, enemy_y))
        """

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


        # Also stolen from game py
        # Player loops around
        # For the X coordinates
        if player_x < 0:
            player_x = WIDTH
        if player_x > WIDTH:
            player_x = 0
        # For the Y coordinates
        if player_y < 0:
            player_y = HEIGHT
        if player_y > HEIGHT:
            player_y = 0


        # Scaling the image to the desired size (should already be at 64x64, this is just in case)
        #player = pygame.transform.scale(player, DEFAULT_PLAYER_SIZE)
        # ROTATION
        #player = pygame.transform.rotate(player, angle=(angle))
        #angle += 1
        # Updating
        #SCREEN.blit(player, (player_x, player_y))

        # Updates the positions of the player and enemy(s)
        player._playerblit_()
        #SCREEN.blit(enemy, (enemy_x, enemy_y))

        # Enemy movement, selects a random number and depending on the range that the number
        # goes into, for a range of 10 (not too sure how it works, but it does)
        # then it increases / decreases the x or y axis by the enemy's velocity
        """
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
        """
        
       
        # Stores the keys pressed
        keys = pygame.key.get_pressed()

        # This was taken from game.py - Don't think the code was taken from anywhere
        # !!! The "and" sections were taken from GeeksForGeeks, see the write-up

        # if a (left) key is pressed 
        if keys[pygame.K_a]: #and player_x> 0: 
            # decrement in x co-ordinate 
            player_x -= player_vel
        # if d (right) key is pressed 
        if keys[pygame.K_d]: #and player_x < WIDTH - 64: 
            # increment in x co-ordinate 
            player_x += player_vel
        # if w (up) key is pressed    
        if keys[pygame.K_w]: #and player_y> 0: 
            # decrement in y co-ordinate 
            player_y -= player_vel
        # if s (down) key is pressed    
        if keys[pygame.K_s]: #and player_y < HEIGHT - 64: 
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