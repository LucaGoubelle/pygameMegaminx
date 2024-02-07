""" entry point """
import sys
import pygame

from megaminx import Megaminx
from megaminx_drawer import MegaminxDrawer

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200,780))
pygame.display.set_caption("pygameMegaminx")
bgcolor = (32,32,32)
# -----------------------
minx = Megaminx(full=True)
minx_drawer = MegaminxDrawer()
# -----------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill(bgcolor)
        #------------------------------
        minx_drawer.draw(screen, minx)
        #------------------------------
        pygame.display.flip()
        clock.tick(60)
