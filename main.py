import sys
import pygame
from gameoflife import GameofLife

pygame.init()
pygame.display.set_caption("Conway's Game of Life")

WIDTH = 1300
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

conway = GameofLife(screen, scale=13)

clock = pygame.time.Clock()
fps = 60


while True:
    clock.tick(fps)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    conway.run()

    pygame.display.update()