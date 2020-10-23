from pygame import *
import pygame
from time import sleep
init()
screen=display.set_mode((1920,1080),pygame.FULLSCREEN,32)
bakeground=image.load("sky.png")
bakeground=transform.scale(bakeground, (1920,1080))
class Spirite(object):
    def __init__(self,temp_screen,x,y,p0,p1):
        self.x=x
        self.y=y
        self.screen=temp_screen
        self.image0 = pygame.image.load(p0)
        self.image1 = pygame.image.load(p1)
        self.rect=self.image1.get_rect()
        self.z=0
    def display(self):
        self.screen.blit(self.image,self.rect) 
    def change(self):
        if self.rect.top>=1080:#rect
            self.rect.top=0
        if self.rect.left>=1920:
            self.rect.left=0
        if self.rect.bottom<=0:
            self.rect.bottom=1080
        if self.rect.right<=0:
            self.rect.right=1980
        if self.z==0:#image
            self.z=1
            self.image=self.image1
        else:
            self.z=0
            self.image=self.image0
class Bullet(Spirite):
    def __init__(self,temp_screen, x, y):
        Spirite.__init__(self,temp_screen,x,y,"0.png","1.png")
        self.rect.bottom=self.y
        self.rect.right=self.x   
    def change(self):
        Spirite.change(self)
        self.rect=self.rect.move([20,0])

class Monster(Spirite):
    def __init__(self,temp_screen):
        Spirite.__init__(self,temp_screen,0,0,"bobo0.png","bobo1.png")
    def move(self):
        
        
class Hero(Spirite):
    def __init__(self,temp_screen):
        Spirite.__init__(self,temp_screen,0,0,"fly-1.png","fly-2.png")
        self.bullet_list = []
    def display(self):
        Spirite.display(self) 
        for bullet in self.bullet_list:
            bullet.change()
            bullet.display()
    def change(self):
        Spirite.change(self)
        self.rect=self.rect.move([self.x,self.y])
        
    def control(self):
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_q:
                    exit()
                if event.key==K_UP:
                    self.y=-10
                if event.key==K_DOWN:
                    self.y=10
                if event.key==K_RIGHT:
                    self.x=10
                if event.key==K_LEFT:
                    self.x=-10
                if event.key==K_SPACE:
                    self.x=0
                    self.y=0
                if event.key==K_0:
                    self.bullet_list.append(Bullet(self.screen, self.rect.right, self.rect.top+50)) 
hero=Hero(screen)
while True:
    screen.blit(bakeground,(0,0))
    hero.change()
    hero.control()
    hero.display()
    display.flip()
    sleep(0.05)
