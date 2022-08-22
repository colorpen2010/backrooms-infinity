import pygame, model

screen = pygame.display.set_mode([1300, 1000])
player1_1 = pygame.image.load('textures backrooms-infinity/player/player 1.png')
player1_2 = pygame.image.load('textures backrooms-infinity/player/player 1-2.png')
player1_3 = pygame.image.load('textures backrooms-infinity/player/player 1-3.png')
player1_4 = pygame.transform.flip(player1_3,True,False)
pygame.display.set_caption("backrooms-infinity")

def scerd():
    pygame.draw.rect(screen, [255, 255, 255], model.fon1_1)
    if model.poworot == 'down':
        screen.blit(player1_1, model.playeri1_1)
    if model.poworot == 'none':
        screen.blit(player1_1, model.playeri1_1)
    if model.poworot == 'up':
        screen.blit(player1_2, model.playeri1_1)
    if model.poworot == 'left':
        screen.blit(player1_4, model.playeri1_1)
    if model.poworot == 'right':
        screen.blit(player1_3, model.playeri1_1)
    pygame.display.flip()
