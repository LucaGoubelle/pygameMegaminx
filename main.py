""" entry point """
import sys;sys.dont_write_bytecode=True
import pygame

from megaminx import Megaminx
from megaminx_scrambler import MegaminxScrambler
from megaminx_drawer import MegaminxDrawer
from moves.mover import Mover

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200,780))
pygame.display.set_caption("pygameMegaminx")
bgcolor = (32,32,32)
# -----------------------
minx = Megaminx(full=True)
minx_drawer = MegaminxDrawer()
minx_mover = Mover()
minx_scrambler = MegaminxScrambler()
# -----------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_u: 
                    minx = minx_mover.simpleMove(minx, "U'") if event.mod & pygame.KMOD_SHIFT else minx_mover.simpleMove(minx, "U")
                case pygame.K_l:
                    minx = minx_mover.simpleMove(minx, "L'") if event.mod & pygame.KMOD_SHIFT else minx_mover.simpleMove(minx, "L")
                case pygame.K_r:
                    minx = minx_mover.simpleMove(minx, "R'") if event.mod & pygame.KMOD_SHIFT else minx_mover.simpleMove(minx, "R")
                case pygame.K_f:
                    minx = minx_mover.simpleMove(minx, "F'") if event.mod & pygame.KMOD_SHIFT else minx_mover.simpleMove(minx, "F")
                case pygame.K_d:
                    minx = minx_mover.simpleMove(minx, "DL'") if event.mod & pygame.KMOD_SHIFT else minx_mover.simpleMove(minx, "DL")
                case pygame.K_b:
                    minx = minx_mover.simpleMove(minx, "BL'") if event.mod & pygame.KMOD_SHIFT else minx_mover.simpleMove(minx, "BL")
                case pygame.K_a:
                    minx = minx_mover.simpleMove(minx, "AL'") if event.mod & pygame.KMOD_SHIFT else minx_mover.simpleMove(minx, "AL")
                case pygame.K_y:
                    minx = minx_mover.simpleMove(minx, "y'") if event.mod & pygame.KMOD_SHIFT else minx_mover.simpleMove(minx, "y")
                case pygame.K_z:
                    minx = minx_mover.simpleMove(minx, "z'") if event.mod & pygame.KMOD_SHIFT else minx_mover.simpleMove(minx, "z")

                case pygame.K_SPACE:
                    minx = minx_scrambler.getScrambledMegaminx(minx_mover, minx)
                case pygame.K_1:
                    minx = minx_mover.multiMove(screen, minx, minx_drawer, "R U R' U'")
                case pygame.K_2:
                    minx = minx_mover.multiMove(screen, minx, minx_drawer, "U R U' R'")
                case pygame.K_3:
                    minx = minx_mover.multiMove(screen, minx, minx_drawer, "R U R'")

        screen.fill(bgcolor)
        #------------------------------
        minx_drawer.draw(screen, minx)
        #------------------------------
        pygame.display.flip()
        clock.tick(60)
