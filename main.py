""" entry point """
import sys
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200,780))
pygame.display.set_caption("pygameMegaminx")
bgcolor = (32,32,32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill(bgcolor)
        pygame.display.flip()
        clock.tick(60)
