import pygame
from pygame import *
from time import sleep
x=0
y=0
init()
screen=display.set_mode((1920,1080),pygame.FULLSCREEN,32)
display.set_caption("hello world")
bakeground=image.load("sky.png")
bakeground=transform.scale(bakeground, (1920,1080))
img=image.load("/home/wing/Pictures/nova.png")
rect=img.get_rect()
screen.blit(img,rect)
display.update()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            print("exit")
            exit()
        elif event.type==KEYDOWN:
            if event.key==K_q:
                exit()
            if event.key==K_UP:
                y=-10
            if event.key==K_DOWN:
                y=10
            if event.key==K_RIGHT:
                x=10
            if event.key==K_LEFT:
                x=-10
            if event.key==K_SPACE:
                x=0
                y=0
    if rect.top==1080:
        rect.top=0
    if rect.left==1920:
        rect.left=0
    if rect.bottom==0:
        rect.bottom=1080
    if rect.right==0:
        rect.right=1980
    rect=rect.move([x,y])
    screen.blit(bakeground,(0,0))
    screen.blit(img,rect)
    display.flip()
    sleep(0.05)
