import pygame,model
player1_1=pygame.image.load('textures backrooms-infinity/player/player 1.png')

def scerd():
    screen = pygame.display.set_mode([1300, 1000])
    pygame.display.set_caption("backrooms-infinity")
    screen.blit(player1_1,model.playeri1_1)
    pygame.display.flip()