import pygame,model
pygame.key.set_repeat(50)
def control():
    coffin_dance = pygame.event.get()
    for i in coffin_dance:
        if i.type == 256:
            exit()
        if i.type == pygame.KEYDOWN and i.key == pygame.K_RIGHT:
            model.poworot = 'right'
            model.right()
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_LEFT:
            model.poworot = 'left'
            model.left()
        if i.type == pygame.KEYDOWN and i.key == pygame.K_UP:
            model.poworot = 'up'
            model.up()
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_DOWN:
            model.poworot = 'down'
            model.down()
