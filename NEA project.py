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

# pygame setup
def main():
    # Initialising things
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("NEA Project")
    WIDTH = 1280
    HEIGHT = 720
    FPS = 60
    SCREEN= pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    running = True
    background_img = pygame.image.load("space-background.png")
    spawner = False

# Test comment
    # Font things
    used_font = pygame.font.SysFont('Helvetica', 30)
    text_surface = used_font.render('Get Collision working; like player and enemies hitting each other', False, 'Red', 'Black')

    # Player things
    DEFAULT_PLAYER_SIZE = (64,64)
    #^^^ The image resoultion used is a 64,64 image.
    player_x = 100
    player_y = 100
    DEFAULT_PLAYER_POS = (player_x,player_y)
    play_vel_x, play_vel_y = 10, 10
    angle = 1

    # Enemy 1 (shooter) things
    enemy_x = random.randint(1, WIDTH)
    enemy_y = random.randint(1, HEIGHT)
    en_vel_x, en_vel_y = 3, 3

    # Mouse config stuff
    # Should hopefully always update the position of the mouse
    mouse_pos = pygame.mouse.get_pos()

    # Test for making player as a class...
    # IT WORKS !!!!! <---- This will backfire in a few attempts
    class Player:
        def __init__(self, player_x, player_y, play_vel_x, play_vel_y,image):
            self.x_pos = player_x
            self.y_pos = player_y
            self.vel_x = play_vel_x
            self.vel_y = play_vel_y
            self.hitbox = pygame.draw.rect(SCREEN,"red", pygame.Rect(player_x, player_y, 64, 64), width=0)
            self.image = image
        def _playerblit_(self):
            SCREEN.blit(self.image, (player_x, player_y))
        def draw_hitbox(self, surface):
            pygame.draw.rect(surface, (0,0,0), self.hitbox)
        def hitbox_movement(self,key):
            if key[pygame.K_a]:
                self.hitbox.move_ip(-10,0)
            if key[pygame.K_d]:
                self.hitbox.move_ip(10,0)
            if key[pygame.K_w]:
                self.hitbox.move_ip(0,-10)
            if key[pygame.K_s]:
                self.hitbox.move_ip(0,10)
    # Hopefully an enemy class
    # Currently unused
    class Enemy:
        def __init__(self):
            self.x_pos = random.randint(1, WIDTH)
            self.y_pos = random.randint(1, HEIGHT)
            self.vel_x = en_vel_x
            self.vel_y = en_vel_y
            self.hitbox = pygame.draw.rect(SCREEN,"green", pygame.Rect(self.x_pos, self.y_pos, 64, 64))
            self.image = pygame.image.load("Test-Enemy.png")
        def _enemyblit_(self):
            SCREEN.blit(self.image, (self.x_pos, self.y_pos))
        def draw_en_hitbox(self, surface):
            pygame.draw.rect(surface, (0,255,0), self.hitbox)
        # ---
        # Code to make the enemy move towards the player - From StackOverflow
        # As such I DO NOT claim credit for this function
        def move_towards_player(self, player_x, player_y):
            # Find direction vector (dx, dy) between enemy and player
            dx, dy = player_x - self.x_pos, player_y - self.y_pos
            # Returns the hypotenuse; the long side, so it's a direct line to the player
            # Not entirely what I want to do, but if it works, then I'll keep it that way unless otherwise
            dist = math.hypot(dx, dy)
            dx, dy = dx / dist, dy / dist # Normalise
            # Move along this normalised vector towards the player at current speed
            self.x_pos += dx * en_vel_x
            self.y_pos += dy * en_vel_y
            # Move the hitbox too
            self.hitbox.move_ip((dx * en_vel_x), 0)
            self.hitbox.move_ip(0, (dy * en_vel_y))
            self._enemyblit_()
        def removal_clicked(self, event_list):
            for event in event_list:
                # If the mouse is clicked and it's on an enemy, remove the enemy - at the moment it's just a print statement just to see if it works :D
                if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos == range(self.x_pos, self.y_pos):
                    print("yeoch")


    # Bullet class
    class Bullet:
        def __init__(self, colour, x, y, width, height, speed, targetx, targety):
            self.rect = pygame.Rect(x,y,width,height)
            self.colour = colour
            self.speed = speed
            self.dx = targetx
            self.dy = targety
        def _bulletblit_(self, SCREEN):
            SCREEN.blit(SCREEN, (self.dx, self.dy))

    bulletlist = []

    def enemy_xory_value_moving(enemy_x, enemy_y, player_x, player_y, enemy_vel):
        if enemy_x < player_x:
            while enemy_x < (player_x + random.randint(10,100)):
                enemy_x += enemy_vel
        elif enemy_y < enemy_y:
            while enemy_y < (player_y + random.randint(10,100)):
                enemy_y += enemy_vel

    # Supposed to draw a bullet but ended up using something else
    def draw_bullet(mx, my, SCREEN):
        colour = (255,255,255)
        bx = 10
        by = 10
        width = 20
        height = 20
        speed = 5
        targetx = mx
        targety = my
        bullet = Bullet(colour, bx, by, width, height, speed, targetx, targety)
        bullet._bulletblit_(SCREEN)

    # Loads the player and the enemy
    plimage = pygame.image.load("Test-Image.png")
    player = Player(player_x, player_y, play_vel_x, play_vel_y, plimage)

    # Putting a max of 5 enemies into a list
    enemy = Enemy()
    enemy2 = Enemy()
    enemy3 = Enemy()
    enemy4 = Enemy()
    enemy5 = Enemy()

    # Adding to list
    enemycontainment = [enemy, enemy2, enemy3, enemy4, enemy5]
    # play around with enemy.surface <- look on pygame
    not_hit_yet = True # For collision

    # Draws a bullet ready to be called
    bullet = pygame.image.load("Test-Bullet.png")

    test_line = pygame.draw.line(SCREEN,"green", (player_x, player_y), (enemy_x, enemy_y))

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                bulletlist.append(event.pos)
                # Adds position to a list
            if event.type == pygame.MOUSEBUTTONUP:
                bulletlist.remove(event.pos)
                # Removes position to a list


        # fill the screen with a color to wipe away anything from last frame
        #SCREEN.fill("orange")
        # set the background from the position 0,0
        SCREEN.blit(background_img, (0,0))
        SCREEN.blit(text_surface, (0,0))

        """ RENDER YOUR GAME HERE """
        # Old code was to spawn in a circle then layer the image on top / override with the image

        # This was part of a post from stackoverflow where it draws every enemy in enemycontainment.
        for enemy in enemycontainment:
            enemy._enemyblit_()
            enemy.draw_en_hitbox(SCREEN)
            if enemy.hitbox.colliderect(player.hitbox):
                not_hit_yet = False
            else:
                not_hit_yet = True
            if not_hit_yet == True:
                enemy.move_towards_player(player_x, player_y)
        
        # eveytime there's a new position in the list, spawn a bullet
        for pos in bulletlist:
            mousex, mousey = pygame.mouse.get_pos()
            test_line = pygame.draw.line(SCREEN,"green", (player_x, player_y), (mousex, mousey))

        #print("Player rect pos", player.hitbox)
        #print("Enemy rect pos", enemy.hitbox)
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

        # Looping for the rect(s)
        # Player
        if player.hitbox.x < 0:
            player.hitbox.x = WIDTH
        if player.hitbox.x > WIDTH:
            player.hitbox.x = 0
        if player.hitbox.y < 0:
            player.hitbox.y = HEIGHT
        if player.hitbox.y > HEIGHT:
            player.hitbox.y = 0

        # Doing the key things
        # Stores the keys pressed
        keys = pygame.key.get_pressed()
        # This was taken from game.py - Don't think the code was taken from anywhere
        # !!! The "and" sections were taken from GeeksForGeeks, see the write-up
        # if a (left) key is pressed 
        if keys[pygame.K_a]: #and player_x> 0: 
            # decrement in x co-ordinate 
            player_x -= play_vel_x
        # if d (right) key is pressed 
        if keys[pygame.K_d]: #and player_x < WIDTH - 64: 
            # increment in x co-ordinate 
            player_x += play_vel_x
        # if w (up) key is pressed    
        if keys[pygame.K_w]: #and player_y> 0: 
            # decrement in y co-ordinate 
            player_y -= play_vel_y
        # if s (down) key is pressed    
        if keys[pygame.K_s]: #and player_y < HEIGHT - 64: 
            # increment in y co-ordinate 
            player_y += play_vel_y
        # Quit Key  
        if keys[pygame.K_q]:
            running = False

        # Updates the positions of the player and enemy(s)
        player._playerblit_()
        player.draw_hitbox(SCREEN)
        player.hitbox_movement(keys)


        # flip() the display to put your work on screen
        pygame.display.flip()

        CLOCK.tick(FPS)  # limits FPS to 60

    pygame.quit()

if __name__ == '__main__':
    main()