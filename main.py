import sys
import pygame
from gameoflife import GameofLife

def launch(init_type='random',fps=60):
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")

    WIDTH = 1300
    HEIGHT = 700

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    conway = GameofLife(screen, scale=13,init_type=init_type)

    clock = pygame.time.Clock()

    while True:
        clock.tick(fps)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        conway.run()
        pygame.display.update()

if __name__== "__main__":
    if len(sys.argv) == 3:
        launch(sys.argv[1],sys.argv[2])
    elif len(sys.argv) == 2:
        launch(sys.argv[1])
    else:
        launch()