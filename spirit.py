from pygame import *
import pygame
from time import sleep
init()
p=0
mixer.init()
sound=pygame.mixer.music.load("lik.wav")
screen=display.set_mode((1920,1080),pygame.FULLSCREEN,32)
bakeground=image.load("竹林.jpg")
bakeground=transform.scale(bakeground, (1920,1080))
background0=image.load("sky.png")
background0=transform.scale(background0, (1920,1080))
monster_list=[]
monster_list_temp=[]
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
    def change(self,x,y):
        Spirite.change(self)
        if self.rect.bottom>=y:
            dy=-1
        else:
            dy=1
        if self.rect.right>=x:
            dx=-1
        else:
            dx=1
        self.rect=self.rect.move([5*dx,5*dy])
        
    def judge(self):
        if self.rect.top>=1080:#rect
            return True
        if self.rect.left>=1920:
            return True
        if self.rect.bottom<=0:
            return True
        if self.rect.right<=0:
            return True
        return False


class Mons(Spirite):
    def __init__(self,temp_screen,p0,p1):
        Spirite.__init__(self,temp_screen,0,0,p0,p1)
    def change(self):
        Spirite.change(self)
        if self.rect.top>=1080:#rect
            self.rect.top=0
        elif self.rect.bottom<=0:
            self.rect.bottom=1080
        if self.rect.left>=1920:
            self.rect.left=0
        elif self.rect.right<=0:
            self.rect.right=1980

class Monster(Mons):
    def __init__(self,temp_screen):
        Mons.__init__(self,temp_screen,"fly-1.png","fly-2.png")
        self.rect.top=500
        self.rect.left=500
    def change(self,x,y):
        Mons.change(self)        
        if self.rect.bottom>=y:
            dy=-1
        else:
            dy=1
        if self.rect.right>=x:
            dx=-1
        else:
            dx=1
        self.rect=self.rect.move([5*dx,5*dy])
    
        
        
monster_list.append(Monster(screen))        
class Hero(Mons):
    def __init__(self,temp_screen):
        Mons.__init__(self,temp_screen,"bobo0.png","bobo1.png")
        self.bullet_list = []
    def display(self):
        Spirite.display(self)
        bullet_list_temp = [] 
        for bullet in self.bullet_list:
            bullet.change(monster_list[0].rect.right,monster_list[0].rect.bottom)
            bullet.display()
            if bullet.judge():#判断子弹是否越界
                bullet_list_temp.append(bullet)

        for bullet in bullet_list_temp:
            self.bullet_list.remove(bullet)
    def change(self):
        Mons.change(self)
        
       
        
    def control(self):
        key=pygame.key.get_pressed()
        if key[K_UP]:self.rect.top-=10
        if key[K_DOWN]:self.rect.top+=10
        if key[K_RIGHT]:self.rect.right+=10
        if key[K_LEFT]:self.rect.right-=10
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_q:
                    exit()
                if event.key==K_0:
                    self.bullet_list.append(Bullet(self.screen, self.rect.right, self.rect.top+50)) 
hero=Hero(screen)

def loop0():
    screen.blit(bakeground,(0,0))
    hero.change()
    hero.control()
    hero.display()
    
    for monster in monster_list:
        monster.change(hero.rect.left,hero.rect.top)
        monster.display()
        for bullet in hero.bullet_list:
            if monster.rect.colliderect(bullet.rect):#判断怪物是否死亡
                mixer.music.play(1)
                hero.bullet_list.remove(bullet)
                if monster in monster_list:
                    monster_list.remove(monster)
    if not monster_list:
        monster_list.append(Monster(screen))
def loop1():
    screen.blit(background0,(0,0))
     
while True:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_p:
                if p==1:
                    p=0
                else:
                    p=1
    if p==0:
        loop0()
    else:
        loop1()
              
    
    
    display.flip()
    sleep(0.05)
