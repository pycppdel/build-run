"""
File from flatterner ---- version 1.0
"""

import pygame

screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("DEMO APP")
fps = 60
ende = False

clock = pygame.time.Clock()

pygame.display.set_caption('THASSILO')
def redraw():
    screen.fill((255, 255, 255))
    pygame.display.flip()

while not ende:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ende = True

    redraw()

pygame.quit()
