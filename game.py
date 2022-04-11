from ast import While
from posixpath import splitdrive
from re import A
from turtle import width
import pygame
import math
import random
pygame.init()


#Screen size
screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))

#Game name
pygame.display.set_caption("Game")

#Animations
player_walk_images = [pygame.image.load("Idle.png"), pygame.image.load("Running.png")]
Skeleton = pygame.image.load("Skeleton.png")
Skeleton2 = pygame.image.load("Skeleton2.png")
Spider = pygame.image.load("Spider.png")
Zombie = pygame.image.load("Zombie.png")
Creepy = pygame.image.load("Creepy.png")

class player:
    def __init__(self, x, y, width, height,):
        #Variables for playable character
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.health = 100
        

        
        #Variables for Dash
        self.dash_distance = 50
        self.cooldown = False
        self.Direction = 1
        #0, Default | 1, Left | 2, Right | 3, Up | 4, Down
        self.dash_cooldown = pygame.USEREVENT + 1
        #Cooldown to check if player is currently dashing
        self.isdashing_cooldown = pygame.USEREVENT + 1
        self.isDashing = False
        #Bullet cooldown
        self.bullet_cooldown = pygame.USEREVENT + 1
        self.bullet_cd = False
        #Damage registration cooldown
        self.reg_cooldown = pygame.USEREVENT + 1
        self.reg_cd = False
        #Player Damage reg cd
        self.player_reg_cooldown = pygame.USEREVENT + 1
        self.player_reg_cd = False
        #Keys
        self.keys = pygame.key.get_pressed()
        
        self.gun_type = 2
        self.gun_speed = 1000
        #Gun Type: 1, Default piston | 2, Smg | 3, Sniper
        
        self.animation_count = 0
        self.moving_right = True
        self.moving_left = False
       
        #player_walk_images = [pygame.transform.scale(pygame.image.load("Idle.png"), (self.height, self.width)), pygame.transform.scale(pygame.image.load("Running.png"), (self.height, self.width))]
        
    def player_animation(self,win):
        if self.animation_count + 1 >= 8:
            self.animation_count = 0
        self.animation_count += 1
        
        #self.mX, self.mY = pygame.mouse.get_pos()
        #self.angleRad = math.atan2(self.y-self.mY, self.mX-self.x)
        #self.angleDeg = math.degrees(self.angleRad)
        
        #win.blit(pygame.transform.rotate(player_walk_images[self.animation_count//4], self.angleRad), (self.x, self.y))
        
        #if self.isDashing == True:
        #    player_walk_images = self.player_dash_images
        if self.moving_right:
            win.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (self.height, self.width)), (self.x, self.y))
        elif self.moving_left:
            win.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[self.animation_count//4], True, False), (self.height, self.width)), (self.x, self.y))
        else:
            if self.Direction == 1:
                win.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[self.animation_count//4], True, False), (self.height, self.width)), (self.x, self.y))
            elif self.Direction == 2:
                win.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (self.height, self.width)), (self.x, self.y))
            elif self.Direction == 3 or self.Direction == 4:
                win.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (self.height, self.width)), (self.x, self.y))
        
        
        self.moving_right = False
        self.moving_left = False

    
        
    def dash(self, win):
        if self.keys[pygame.K_e] and self.cooldown == False:
            self.cooldown = True
            self.isDashing = True
            pygame.time.set_timer(self.dash_cooldown, 4000)
            pygame.time.set_timer(self.isdashing_cooldown, 750)
            
            #Checks for direction and according to it dashes to that direction
            if self.Direction == 1:
                if self.x > self.dash_distance:
                    self.x -= self.dash_distance
            elif self.Direction == 2:
                if self.x < screenWidth - self.width - self.dash_distance:
                    self.x += self.dash_distance
            elif self.Direction == 3:
                if self.y > self.dash_distance:
                    self.y -= self.dash_distance
            elif self.Direction == 4:
                if self.y < screenHeight - self.height - self.dash_distance:
                    self.y += self.dash_distance
                    
    
                    
    def movment(self, win):
        self.keys = pygame.key.get_pressed()
    
        #Movement system if button is pressed goes to a direction untill player is close to sides and then stops
        if self.keys[pygame.K_LEFT] or self.keys[pygame.K_a] and  self.x > self.vel:
            self.x -= self.vel
            self.Direction = 1
            self.moving_left = True 
        if self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d] and self.x < screenWidth - self.width - self.vel:
            self.x += self.vel
            self.Direction = 2
            self.moving_right = True
        if self.keys[pygame.K_UP] or self.keys[pygame.K_w] and self.y > self.vel:
            self.y -= self.vel
            self.Direction = 3
        if self.keys[pygame.K_DOWN] or self.keys[pygame.K_s] and self.y < screenHeight - self.height - self.vel:
            self.y+= self.vel
            self.Direction = 4   
    
    def damage_player(self, win):
        
        
        if enemy.x < (self.x + self.width/2) < (enemy.x + enemy.width) and (enemy.y + enemy.height)> (self.y + self.height/2) > enemy.y and self.player_reg_cd == False:
            self.player_reg_cd = True
            pygame.time.set_timer(iden.player_reg_cooldown, 500)
            
            self.health -= enemy.damage
            print("Iden Health: ", self.health)
            
            
            if iden.health == 0:
                print("Game Over")
    
    def gun_switching(self,win):
        if self.keys[pygame.K_1]:
            self.gun_type = 1
            print("Gun Type: ", self.gun_type)
        if self.keys[pygame.K_2]:
            self.gun_type = 2
            print("Gun Type: ", self.gun_type)
        if self.keys[pygame.K_3]:
            self.gun_type = 3
            print("Gun Type: ", self.gun_type)
            
        
    def events(self,win):
        #Check for event
        for event in pygame.event.get():
        #Cooldown for dash
            if event.type == self.dash_cooldown:
                self.cooldown = False
                pygame.time.set_timer(self.dash_cooldown, 0)
        #Cooldown for checking if player is currently dashing        
            if event.type == self.isdashing_cooldown:
                self.isDashing = False
                pygame.time.set_timer(self.isdashing_cooldown, 0)
        #Cooldown for bullet firing        
            if event.type == self.bullet_cooldown:
                self.bullet_cd = False
                pygame.time.set_timer(self.bullet_cooldown, 0)
        #Cooldown for damage registration
            if event.type == self.reg_cooldown:
                self.reg_cd = False
                pygame.time.set_timer(self.reg_cooldown, 0)
        #Cooldown for player damage registration
            if event.type == self.player_reg_cooldown:
                self.player_reg_cd = False
                pygame.time.set_timer(self.player_reg_cooldown, 0)
        #Closes window if X is pressed               
            elif event.type == pygame.QUIT:
                self.run = False  
        #Creates a bullet and starts timer for next one if player is not dashing and cooldown is off        
            if event.type == pygame.MOUSEBUTTONDOWN and self.isDashing == False and self.bullet_cd == False:
                self.bullet_cd = True
                pygame.time.set_timer(self.bullet_cooldown, self.gun_speed)
                player_bullets.append(PlayerBullet(self.x, self.y, mouse_x, mouse_y))

#Class for creating the bullet that the player shoots                
class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 30
        self.width = 40
        self.height = 60
        #Calculating angle to move bullet to according to the mouse
        self.angle = math.atan2(y-mouse_y, x-mouse_x + (self.width/2))
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    
    def main(self, win):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        
        #Draws the object for the bullet
        win.blit(pygame.transform.scale(pygame.image.load("Bullet.png"), (12, 12)), (self.x, self.y + (iden.width//2)))
        #pygame.draw.circle(win, (0, 0, 255), (self.x + (self.width/2), self.y), 5)
        
            
            
class Enemy:
    def __init__(self, x, y, height, width, health, damage, vel):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = vel
        self.health = health
        self.damage = damage
        self.moving_right = True
        self.moving_left = False
        
        
    def main(self, win):   
        self.enemy_x = random.randint(0, screenWidth)
        self.enemy_y = random.randint(0, screenHeight)
        
        #pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))
        #enemy_list.append(Enemy(self.x, self.y, self.width, self.height))
        
        
        self.enemy_top_right = self.x + enemy.width
        self.enemy_top_left = self.x
        self.enemy_bottom_right = (self.x + enemy.width) - enemy.height
        self.enemy_bottom_right = self.y - enemy.height
        
    def enemy_movement(self, win):
        
        if iden.x > self.x:
            self.x += self.vel
            self.moving_right = True
        if iden.x < self.x:
            self.x -= self.vel
            self.moving_left = True
        if iden.y > self.y:
            self.y += self.vel
        if iden.y < self.y:
            self.y -= self.vel
    
    def damage_enemy(self,win):
        
        
        if enemy.x < bullet.x < (enemy.x + enemy.width) and (enemy.y + enemy.height) > bullet.y > enemy.y and iden.reg_cd == False:
            iden.reg_cd = True
            pygame.time.set_timer(iden.reg_cooldown, 400) 
            
            #Pistol
            if iden.gun_type == 1:
                bullet.speed = 30
                iden.gun_speed = 1000
                enemy.health -= 35
                print(enemy.health)
                if bullet in player_bullets:
                    player_bullets.remove(bullet)
                if enemy.health <= 0:
                    enemy_list.remove(enemy)
                    
                        
            #SMG        
            if iden.gun_type == 2:
                bullet.speed = 45
                iden.gun_speed = 500
                enemy.health -= 25
                print(enemy.health)
                if bullet in player_bullets:
                    player_bullets.remove(bullet)
                if enemy.health <= 0:
                    enemy_list.remove(enemy)
                        
                        
            #Sniper
            if iden.gun_type == 3:
                bullet.speed = 60
                iden.gun_speed = 2500
                enemy.health -= 100
                print(enemy.health)
                if enemy.health <= 0:
                    enemy_list.remove(enemy)    
                    
    def enemy_animation(self,win):
        if self.vel == 3:
            if self.moving_right:
                win.blit(pygame.transform.scale(pygame.transform.flip(Skeleton2, True, False), (self.width*2.5, self.height*1.1)), (self.x - 5, self.y))
            elif self.moving_left:
                 win.blit(pygame.transform.scale(Skeleton2, (self.width*2.5, self.height*1.1)), (self.x - 5, self.y))
            else:
                win.blit(pygame.transform.scale(pygame.transform.flip(Skeleton2, True, False), (self.width*2.5, self.height*1.1)), (self.x - 5, self.y))
        if self.vel == 5.5:
            if self.moving_right:
                win.blit(pygame.transform.scale(pygame.transform.flip(Zombie, True, False), (self.width * 1.4, self.height * 1.3)), (self.x - 5, self.y))
            elif self.moving_left:
                 win.blit(pygame.transform.scale(Zombie, (self.width * 1.4, self.height * 1.3)), (self.x, self.y))
            else:
                win.blit(pygame.transform.scale(pygame.transform.flip(Zombie, True, False), (self.width * 1.4, self.height * 1.3)), (self.x - 5, self.y))
        if self.vel == 3.25:
            if self.moving_right:
                win.blit(pygame.transform.scale(pygame.transform.flip(Skeleton, True, False), (self.width * 1.9, self.height * 1.1)), (self.x - 7, self.y - 2))
            elif self.moving_left:
                 win.blit(pygame.transform.scale(Skeleton, (self.width* 1.9, self.height * 1.1)), (self.x - 10, self.y - 2))
            else:
                win.blit(pygame.transform.scale(pygame.transform.flip(Skeleton, True, False), (self.width* 1.9, self.height * 1.1), (self.x - 7, self.y - 2)))
        if self.vel == 2.5:
            if self.moving_right:
                win.blit(pygame.transform.scale(pygame.transform.flip(Creepy, True, False), (self.width, self.height)), (self.x, self.y))
            elif self.moving_left:
                 win.blit(pygame.transform.scale(Creepy, (self.width, self.height)), (self.x, self.y))
            else:
                win.blit(pygame.transform.scale(pygame.transform.flip(Creepy, True, False), (self.width, self.height)), (self.x, self.y))
        self.moving_right = False
        self.moving_left = False

                
class Timer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.secs = 0
        self.mins = 0
        self.tens = 0
        self.font = pygame.font.Font("pixel.ttf", 32)
        self.text = self.font.render("{}{}:{}".format(self.tens, self.mins, self.secs), True, (255,255,255), (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = screenWidth//2, 32

        self.clock = pygame.time.Clock()


#Creating lists for the bullets and enemies 
player_bullets = []
enemy_list = []
enemy_spawn = 2
rare_enemy_spawn = 8
epic_enemy_spawn = 25
boss_enemy_spawn = 1
#mainloop  
              
start_ticks = pygame.time.get_ticks()              
              
clock = pygame.time.Clock()                    
#X, Y, Width, Height
timer = Timer(10, 10)
bullet = PlayerBullet(1, 1, 1, 1)
iden = player(50, 425, 54, 60)
enemy = Enemy(random.randint(1, 500), random.randint(1, 400), 60, 30, 100, 10, 3)

iden.run = True
while iden.run:
    pygame.time.delay(100)
       
    #Second Counter
    seconds = (pygame.time.get_ticks() - start_ticks)/990  
    secs = (pygame.time.get_ticks() - start_ticks)/990  
       
    mouse_x, mouse_y = pygame.mouse.get_pos() 
       
    iden.events(win)
    iden.movment(win)    
    iden.dash(win)
    iden.gun_switching(win)
    
    
    #Window color
    win.fill((0, 0, 0))
    
    #Checks if there is a bullet or enemy in the list of bullets/enemies and then updates the screen if there is one
    for bullet in player_bullets:
        bullet.main(win)
        
        #removing bullet if out of screen
        if bullet.x > screenWidth:
            player_bullets.remove(bullet)
        elif bullet.x < 0:
            player_bullets.remove(bullet)
        elif bullet.y > screenHeight:
            player_bullets.remove(bullet)
        elif bullet.y < 0:
            player_bullets.remove(bullet)
        
    for enemy in enemy_list:
        enemy.main(win)
        enemy.enemy_movement(win)
        enemy.damage_enemy(win)
        enemy.enemy_animation(win)
        iden.damage_player(win)

    #self, x, y, height, width, health, damage, vel
    if round(seconds, 1) == enemy_spawn:
        enemy_list.append(Enemy(random.randint(1, 500), random.randint(1, 400), 60, 30, 100, 10, 3))
        enemy_spawn += 4
    if round(seconds, 1) == rare_enemy_spawn:
        rare_enemy_spawn += 8
        rng = random.randint(1, 10)
        print("rng is:", rng)
        if rng <= 5:
            enemy_list.append(Enemy(random.randint(1, 500), random.randint(1, 400), 50, 40, 75, 10, 5.5))
            rng = random.randint(1, 10)
            if rng <= 5:
                enemy_list.append(Enemy(random.randint(1, 500), random.randint(1, 400), 50, 40, 75, 10, 5.5))
    if round(seconds, 1) == epic_enemy_spawn:
        epic_enemy_spawn += 25
        rng = random.randint(1, 10)
        print("rng is:", rng)
        if rng >= 5:
            enemy_list.append(Enemy(random.randint(1, 500), random.randint(1, 400), 70, 40, 200, 20, 3.25))
    if round(seconds, 1) == boss_enemy_spawn:
        boss_enemy_spawn += 30
        rng = random.randint(1, 10)
        print("rng is:", rng)
        if rng == 5 or rng == 3:
            enemy_list.append(Enemy(random.randint(1, 500), random.randint(1, 400), 70, 70, 400, 40, 2.5))
            
    print(round(seconds, 1), enemy_spawn)

        

    iden.player_animation(win)    
    #pygame.draw.rect(win, (255, 0, 0), (iden.x, iden.y, iden.width, iden.height))
    
    pygame.draw.rect(win, (122, 133, 131), (25, 20, 125, 30))
    pygame.draw.rect(win, (222, 9, 41), (30, 25, iden.health * 1.15, 20))

    win.blit(timer.text, timer.textRect)
    pygame.display.update()

    timer.secs += 0.1
    if timer.secs >= 60:
        timer.secs = 0
        timer.mins += 1
    if timer.mins >= 10:
        timer.mins = 0
        timer.tens += 1
    timer.text = timer.font.render("{}{}:{}".format(timer.tens, timer.mins, math.floor(timer.secs)), True, (255,255,255), (0, 0, 0))
    clock.tick(60)
    
pygame.quit()
