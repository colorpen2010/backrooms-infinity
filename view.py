import pygame, model

screen = pygame.display.set_mode([1300, 1000])
player1_1 = pygame.image.load('textures backrooms-infinity/player/player 1.png')
player1_2 = pygame.image.load('textures backrooms-infinity/player/player 1.png')
pygame.display.set_caption("backrooms-infinity")

def scerd():
    pygame.draw.rect(screen, [255, 255, 255], model.fon1_1)
    screen.blit(player1_1, model.playeri1_1)
    pygame.display.flip()
