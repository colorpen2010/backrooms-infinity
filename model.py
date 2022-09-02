import pygame
playeri1_1=pygame.Rect(1300/2,1000/2,100,100)
backrooms_walls=pygame.Rect(400,500,400,300)
fon1_1=pygame.Rect(0,0,1300,1000)
poworot='none'
moved = 1
movea = -1
def up():
    playeri1_1.y -= 10

def down():
    playeri1_1.y += 10

def right():
    playeri1_1.x += 10

def left():
    playeri1_1.x -= 10