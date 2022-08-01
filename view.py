import pygame
player1_1=pygame.image.load('textures backrooms-infinity/player/player 1.png')
playeri1_1=pygame.Rect(100,100,100,100)
def scerd():
    screen = pygame.display.set_mode([1300, 1000])
    pygame.display.set_caption("backrooms-infinity")
    screen.blit(player1_1,playeri1_1)
    pygame.display.flip()