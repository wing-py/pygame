from pygame import *
import pygame
from time import sleep
init()
screen=display.set_mode((1920,1080),pygame.FULLSCREEN,32)
bakeground=image.load("sky.png")
bakeground=transform.scale(bakeground, (1920,1080))

class Hero(object):
    def __init__(self,temp_screen):
        self.screen=temp_screen
        self.img1=image.load("fly-1.png")
        self.img2=image.load("fly-2.png")
        self.rect=self.img1.get_rect()
        self.x=0
        self.y=0
        self.z=0
    def display(self):
        self.screen.blit(self.image, self.rect) 
    def change(self):
        if self.rect.top==1080:#rect
            self.rect.top=0
        if self.rect.left==1920:
            self.rect.left=0
        if self.rect.bottom==0:
            self.rect.bottom=1080
        if self.rect.right==0:
            self.rect.right=1980
        self.rect=self.rect.move([self.x,self.y])
        if self.z==0:#image
            self.z=1
            self.image=self.img1
        else:
            self.z=0
            self.image=self.img2
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
 
hero=Hero(screen)
while True:
    screen.blit(bakeground,(0,0))
    hero.change()
    hero.control()
    hero.display()
    display.flip()
    sleep(0.05)
