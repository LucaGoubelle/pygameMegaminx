""" mover """
import pygame

from moves.std_moves import *
from moves.axis_moves import *
from moves.back_moves import *
from moves.abs_moves import *
from moves.down_moves import *

class Mover:
    """ mover """
    def __init__(self):
        pass
    
    def sleeper(t):
        # t = millisecond
        pygame.time.wait(t)
    
    def multiMove(self, scr, minx, md, s, delay=200):
        lstMove = s.split(" ")
        for i in range(len(lstMove)):
            match lstMove[i]:
                case "U": minx = move_U(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "U'": minx = move_U_prime(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "U2": minx = move_U2(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "L": minx = move_L(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "L'": minx = move_L_prime(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "L2": minx = move_L2(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "R": minx = move_R(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "R'": minx = move_R_prime(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "R2": minx = move_R2(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "F": minx = move_F(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "F'": minx = move_F_prime(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "F2": minx = move_F2(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "DL": minx = move_DL(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "DL'": minx = move_DL_prime(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "DL2": minx = move_DL2(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "DR": minx = move_DR(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "DR'": minx = move_DR_prime(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "DR2": minx = move_DR2(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "BL": minx = move_BL(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "BL'": minx = move_BL_prime(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "BL2": minx = move_BL2(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "BR": minx = move_BR(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "BR'": minx = move_BR_prime(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "BR2": minx = move_BR2(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "AL": minx = move_AL(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "AL'": minx = move_AL_prime(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "AL2": minx = move_AL2(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "AR": minx = move_AR(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "AR'": minx = move_AR_prime(minx); md.draw(scr, minx); Mover.sleeper(delay)
                case "AR2": minx = move_AR2(minx); md.draw(scr, minx); Mover.sleeper(delay)
        return minx
