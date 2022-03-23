from ast import While
from re import A
from turtle import width
import pygame
import math
pygame.init()

##### NO ANIMATION ######

#Screen size
screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))

#Game name
pygame.display.set_caption("Game")

class player(object):
    def __init__(self, x, y, width, height,):
        #Variables for playable character
        self.x = 50
        self.y = 425
        self.width = width
        self.height = height
        self.vel = 10

        
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
        #Keys
        self.keys = pygame.key.get_pressed()
        

    
        
    def dash(self,win):
        if self.keys[pygame.K_e] and self.cooldown == False:
            self.cooldown = True
            self.isDashing = True
            pygame.time.set_timer(self.dash_cooldown, 10)
            pygame.time.set_timer(self.isdashing_cooldown, 300)
            
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
                    
    def movment(self,win):
        self.keys = pygame.key.get_pressed()
    
        #Movement system if button is pressed goes to a direction untill player is close to sides and then stops
        if self.keys[pygame.K_LEFT] or self.keys[pygame.K_a] and  self.x > self.vel:
            self.x -= self.vel
            self.Direction = 1 
        if self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d] and self.x < screenWidth - self.width - self.vel:
            self.x += self.vel
            self.Direction = 2
        if self.keys[pygame.K_UP] or self.keys[pygame.K_w] and self.y > self.vel:
            self.y -= self.vel
            self.Direction = 3
        if self.keys[pygame.K_DOWN] or self.keys[pygame.K_s] and self.y < screenHeight - self.height - self.vel:
            self.y+= self.vel
            self.Direction = 4   
  
        
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
        #Closes window if X is pressed               
            elif event.type == pygame.QUIT:
                self.run = False  
        #Creates a bullet and starts timer for next one if player is not dashing and cooldown is off        
            if event.type == pygame.MOUSEBUTTONDOWN and self.isDashing == False and self.bullet_cd == False:
                self.bullet_cd = True
                pygame.time.set_timer(self.bullet_cooldown, 1000)
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
        pygame.draw.circle(win, (0,0,255), (self.x + (self.width/2), self.y), 5)
        pygame.display.update()
            
class Enemy:
    def __init__(self, x, y):
        self.x = 100
        self.y = 400
        self.height = 60
        self.width = 40
        self.vel = 3
        
    def main(self, win):    
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))
        #enemy_list.append(Enemy(self.x, self.y, self.width, self.height))
        pygame.display.update()          
        
 
#Creating lists for the bullets and enemies 
player_bullets = []
enemy_list = []
 
#mainloop   
              
clock = pygame.time.Clock()                    
#X, Y, Width, Height
iden = player(40, 40, 40, 60)
iden.run = True
while iden.run:
    pygame.time.delay(100)
       
    mouse_x, mouse_y = pygame.mouse.get_pos() 
       
    iden.events(win)
    iden.movment(win)    
    iden.dash(win)

    #Window color
    win.fill((0, 0, 0))
    #Chracter size & color
    pygame.draw.rect(win, (255, 0, 0), (iden.x, iden.y, iden.width, iden.height))
    pygame.display.update()
    
    #Checks if there is a bullet or enemy in the list of bullets/enemies and then updates the screen if there is one
    for bullet in player_bullets:
        bullet.main(win)
    for enemy in enemy_list:
        enemy.main(win)
    
    clock.tick(60)
    
pygame.quit()
