""" entry point """
import sys;sys.dont_write_bytecode=True
import pygame

from megaminx.megaminx import Megaminx
from megaminx.megaminx_scrambler import MegaminxScrambler
from megaminx.megaminx_drawer import MegaminxDrawer
from megaminx.moves.mover import Mover

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200,780))
pygame.display.set_caption("pygameMegaminx")
bgcolor = (32,32,32)
# -----------------------
minx = Megaminx(full=True)
minx_drawer = MegaminxDrawer()
minx_mover = Mover(minx_drawer, screen)
minx_scrambler = MegaminxScrambler()
# -----------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_m: minx = minx_mover.simpleMove(minx, "U'")
                case pygame.K_k: minx = minx_mover.simpleMove(minx, "U")
                case pygame.K_z: minx = minx_mover.simpleMove(minx, "L'")
                case pygame.K_s: minx = minx_mover.simpleMove(minx, "L")
                case pygame.K_l: minx = minx_mover.simpleMove(minx, "R'")
                case pygame.K_o: minx = minx_mover.simpleMove(minx, "R")
                case pygame.K_f: minx = minx_mover.simpleMove(minx, "F'") 
                case pygame.K_j: minx = minx_mover.simpleMove(minx, "F")
                case pygame.K_q: minx = minx_mover.simpleMove(minx, "DL'") 
                case pygame.K_d: minx = minx_mover.simpleMove(minx, "DL")
                case pygame.K_RIGHT: minx = minx_mover.simpleMove(minx, "y'")
                case pygame.K_LEFT: minx = minx_mover.simpleMove(minx, "y")
                case pygame.K_UP: minx = minx_mover.simpleMove(minx, "z'")
                case pygame.K_DOWN: minx = minx_mover.simpleMove(minx, "z")

                case pygame.K_SPACE: minx = minx_scrambler.getScrambledMegaminx(minx_mover, minx)
                case pygame.K_ESCAPE: minx = Megaminx(full=True)

                case pygame.K_1: minx = minx_mover.multiMove(minx, "R U R' U'")
                case pygame.K_2: minx = minx_mover.multiMove(minx, "U R U' R'")
                case pygame.K_3: minx = minx_mover.multiMove(minx, "R U R'")

        screen.fill(bgcolor)
        #------------------------------
        minx_drawer.draw(screen, minx)
        #------------------------------
        pygame.display.flip()
        clock.tick(60)
