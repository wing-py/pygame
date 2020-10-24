from pygame import *
from time import sleep
import pygame

init()
class Plant(object):
    def __init__(self,temp_screen,x,y):
        self.x=0
        self.y=0
        self.t=0
        self.screen=temp_screen
        self.image0 = pygame.image.load("seed.png")
        self.image=self.image0
        self.image1 = pygame.image.load("bud.png")
        self.image2 = pygame.image.load("flower.png")
        self.image3 = pygame.image.load("harvest.png")
        self.rect=self.image0.get_rect()
        self.rect.top=y*250
        self.rect.left=x*250
    def display(self):
        self.screen.blit(self.image,self.rect)
    def change(self):
        self.t+=1
        if self.t>=100:
            self.image=self.image3
        elif self.t>=75:
            self.image=self.image2
        elif self.t>=50:
            self.image=self.image1

            
   
class Farmer(object):
    def __init__(self,temp_screen):
        self.x=0
        self.y=0
        self.z=0
        self.screen=temp_screen
        self.image = pygame.image.load("bobo0.png")
        self.rect=self.image.get_rect()
        self.plant_list=[]
    def display(self):
        for plant in self.plant_list:
            plant.change()
            plant.display()
            if self.rect.colliderect(plant.rect) and plant.t>=100:
                self.plant_list.remove(plant)
                self.z+=1
                print(self.z)
                
        self.screen.blit(self.image,self.rect)
    def change(self):
        for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_q:
                        print("exit")
                        exit()
                    if event.key==K_UP:
                        if self.y==0:
                            self.y=3
                        else:
                            self.y-=1                           
                    elif event.key==K_DOWN:
                        if self.y==3:
                            self.y=0
                        else:
                            self.y+=1
                    if event.key==K_LEFT:
                        if self.x==0:
                            self.x=3
                        else:
                            self.x-=1
                    elif event.key==K_RIGHT:
                        if self.x==3:
                            self.x=0
                        else:
                            self.x+=1
                    if event.key==K_SPACE:
                        self.plant_list.append(Plant(self.screen,self.x,self.y))
                    
      
        self.rect.top=self.y*250
        self.rect.left=self.x*250
    
        
                    
screen=display.set_mode((1920,1080),FULLSCREEN,32)
bakeground=image.load("竹林.jpg")
bakeground=transform.scale(bakeground, (1920,1080))
screen.blit(bakeground,(0,0))
none=image.load("none.png")
none=transform.scale(none,(200,200))  
farmer=Farmer(screen)  
def loop():
    screen.blit(bakeground,(0,0))
    for i in range(4):
        
        for j in range(4):
            
            screen.blit(none,(i*250,j*250))
    farmer.change()
    farmer.display()
    
    display.flip()
    sleep(0.05)
while True:
    loop()
