""" mover """
import pygame

from moves.std_moves import *
from moves.axis_moves import *
from moves.back_moves import *
from moves.abs_moves import *
from moves.down_moves import *
from moves.scramble_moves import *

class Mover:
    """ mover """
    def __init__(self):
        pass
    
    def sleeper(t):
        # t = millisecond
        pygame.time.wait(t)
        
    def simpleMove(self, minx, move):
        match move:
            case "U": minx = move_U(minx)
            case "U'": minx = move_U_prime(minx)
            case "U2": minx = move_U2(minx)
            case "L": minx = move_L(minx)
            case "L'": minx = move_L_prime(minx)
            case "L2": minx = move_L2(minx)
            case "R": minx = move_R(minx)
            case "R'": minx = move_R_prime(minx)
            case "R2": minx = move_R2(minx)
            case "F": minx = move_F(minx)
            case "F'": minx = move_F_prime(minx)
            case "F2": minx = move_F2(minx)
            case "DL": minx = move_DL(minx)
            case "DL'": minx = move_DL_prime(minx)
            case "DL2": minx = move_DL2(minx)
            case "DR": minx = move_DR(minx)
            case "DR'": minx = move_DR_prime(minx)
            case "DR2": minx = move_DR2(minx)
            case "BL": minx = move_BL(minx)
            case "BL'": minx = move_BL_prime(minx)
            case "BL2": minx = move_BL2(minx)
            case "BR": minx = move_BR(minx)
            case "BR'": minx = move_BR_prime(minx)
            case "BR2": minx = move_BR2(minx)
            case "AL": minx = move_AL(minx)
            case "AL'": minx = move_AL_prime(minx)
            case "AL2": minx = move_AL2(minx)
            case "AR": minx = move_AR(minx)
            case "AR'": minx = move_AR_prime(minx)
            case "AR2": minx = move_AR2(minx)
            case "y": minx = move_y(minx)
            case "y'": minx = move_y_prime(minx)
            case "z": minx = move_z(minx)
            case "z'": minx = move_z_prime(minx)
            case "R++": minx = move_RPP(minx)
            case "R--": minx = move_RMM(minx)
            case "D++": minx = move_DPP(minx)
            case "D--": minx = move_DMM(minx)
        return minx
    
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
