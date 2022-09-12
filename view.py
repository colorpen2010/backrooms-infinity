import pygame, model

screen = pygame.display.set_mode([1300, 1000])
player1_1 = pygame.image.load('textures backrooms-infinity/player/player 1.png')
player1_2 = pygame.image.load('textures backrooms-infinity/player/player 1-2.png')
player1_3 = pygame.image.load('textures backrooms-infinity/player/player 1-3.png')
player1_4 = pygame.transform.flip(player1_3, True, False)


bakrooms_level_0_walls = pygame.image.load('textures backrooms-infinity/wals/wals_level_0.png')
bakrooms_level_0_walls1 = pygame.Surface([model.backrooms_walls.width, model.backrooms_walls.height])  # создаёт чёрную картинку размером 100 на 100
bakrooms_level_0_walls1.blit(bakrooms_level_0_walls, [0, 0])


pygame.display.set_caption("backrooms-infinity")

def scerd():
    pygame.draw.rect(screen, [255, 255, 255], model.fon1_1)
    for v_walls in model.walls:
        pygame.draw.rect(screen, [0, 0, 0], v_walls)
    # screen.blit(bakrooms_level_0_walls1, model.backrooms_walls)
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
