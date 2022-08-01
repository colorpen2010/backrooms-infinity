import pygame
def control():
    coffin_dance = pygame.event.get()
    for i in coffin_dance:
        if i.type == 256:
            exit()