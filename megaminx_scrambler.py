""" megaminx scrambler """
from random import randint

class MegaminxScrambler:
    
    def __init__(self):
        self.scrambleList = [
            "D++ R++ D++ R++ D++ R++ D++ R-- D-- R-- U R++ D++ R++ D++ R++ D++ R-- D++ R++ D++ U R++ D-- R++ D-- R-- D++ R-- D-- R++ D-- U' D-- R++ D-- R++ D++ R++ D++ R++ D-- R-- U D-- R++ D++ R-- D-- R++ D++ R-- D++ R++ U' D-- R-- D-- R++ D-- R++ D++ R-- D-- R++ U R-- D++ R-- D++ R-- D++ R++ D-- R-- D++ U'",
            "D-- R++ D-- R++ D++ R-- D-- R++ D-- R-- U R++ D++ R++ D-- R-- D-- R-- D-- R++ D-- U' R++ D++ R++ D-- R++ D-- R++ D++ R++ D++ U D++ R-- D-- R++ D++ R++ D++ R++ D++ R++ U' D-- R-- D++ R++ D++ R++ D++ R++ D++ R++ U' D-- R-- D++ R++ D-- R-- D++ R-- D++ R++ U D-- R-- D++ R++ D++ R++ D++ R-- D-- R-- U'",
            "D++ R-- D-- R-- D-- R-- D-- R-- D++ R++ U' R-- D-- R++ D++ R++ D-- R-- D-- R++ D-- U D-- R++ D-- R++ D++ R-- D++ R++ D-- R++ U D++ R-- D-- R++ D-- R++ D-- R++ D++ R-- U D-- R-- D++ R++ D-- R++ D++ R++ D-- R-- U' D-- R-- D-- R++ D++ R++ D-- R-- D-- R-- U' R++ D-- R-- D-- R-- D++ R-- D-- R-- D++ U",
            "D++ R++ D-- R-- D++ R++ D++ R-- D++ R++ U' R++ D++ R++ D++ R++ D-- R-- D-- R++ D++ U' R++ D++ R-- D-- R-- D++ R-- D-- R-- D-- U D++ R++ D++ R-- D++ R++ D-- R-- D-- R-- U' D-- R++ D-- R++ D-- R++ D-- R-- D-- R-- U' D++ R-- D++ R++ D-- R-- D-- R-- D++ R++ U R-- D-- R-- D++ R++ D-- R-- D++ R-- D++ U'",
            "D-- R++ D++ R++ D++ R++ D-- R-- D++ R-- U R-- D-- R-- D-- R++ D-- R-- D++ R-- D-- U' D-- R++ D++ R++ D++ R++ D-- R-- D++ R-- U R-- D-- R++ D++ R++ D++ R++ D++ R-- D-- U' D-- R++ D-- R++ D-- R++ D-- R++ D++ R-- U D++ R++ D-- R++ D++ R++ D++ R-- D++ R++ U R++ D-- R-- D++ R-- D++ R-- D++ R++ D-- U'",
            
            "D++ R-- D++ R-- D++ R++ D++ R-- D-- R-- U' R++ D-- R-- D-- R++ D-- R++ D-- R-- D-- U' D-- R++ D++ R-- D++ R-- D++ R++ D-- R++ U' D++ R-- D++ R-- D-- R++ D++ R++ D++ R-- U' R-- D++ R++ D++ R++ D++ R-- D++ R++ D++ U D++ R++ D++ R-- D++ R-- D-- R-- D++ R-- U' D++ R++ D-- R++ D++ R++ D++ R++ D++ R-- U",
            "R++ D++ R-- D-- R++ D-- R-- D++ R-- D-- U' D++ R-- D-- R-- D++ R++ D-- R++ D-- R-- U' D-- R-- D++ R-- D++ R-- D-- R++ D-- R-- U' D-- R-- D-- R++ D-- R-- D++ R-- D-- R++ U' D-- R++ D++ R++ D++ R-- D++ R-- D++ R++ U' R-- D-- R++ D++ R-- D-- R-- D-- R-- D++ U D++ R-- D-- R-- D++ R-- D-- R++ D++ R++ U'",
            "R-- D-- R++ D++ R++ D-- R++ D-- R++ D++ U D++ R++ D++ R-- D++ R++ D-- R-- D++ R++ U D-- R++ D++ R-- D-- R++ D-- R-- D-- R++ U' D++ R-- D-- R++ D-- R-- D++ R-- D++ R-- U' D-- R++ D-- R++ D++ R++ D++ R-- D++ R-- U D-- R-- D-- R-- D-- R++ D-- R++ D-- R-- U R++ D-- R-- D-- R++ D++ R++ D-- R-- D-- U'",
            "R++ D++ R-- D++ R-- D-- R-- D++ R-- D-- U' R++ D-- R++ D++ R-- D++ R++ D-- R-- D-- U' D-- R-- D++ R-- D-- R-- D++ R-- D-- R-- U' D++ R-- D++ R++ D-- R++ D++ R-- D++ R++ U' R-- D-- R++ D++ R-- D-- R-- D++ R++ D++ U' D-- R-- D-- R++ D++ R++ D-- R++ D-- R-- U' D++ R-- D++ R-- D++ R++ D++ R-- D-- R-- U'",
            "D-- R-- D-- R-- D++ R++ D++ R++ D-- R++ U D-- R++ D-- R++ D-- R++ D-- R-- D-- R++ U' R-- D++ R++ D++ R++ D++ R-- D++ R-- D++ U' D-- R-- D-- R-- D++ R++ D++ R++ D++ R++ U D++ R-- D++ R-- D++ R++ D++ R-- D-- R-- U' R-- D++ R++ D++ R++ D-- R++ D-- R++ D-- U D++ R-- D-- R-- D-- R++ D-- R-- D++ R-- U"
        ]
        
    def getAllMoves(s):
        return s.split()
    
    def scrambleMegaminx(minx, mover, scramble):
        scrambleLst = MegaminxScrambler.getAllMoves(scramble)
        for mv in scrambleLst:
            match mv:
                case "U": minx = mover.simpleMove(minx, "U")
                case "U'": minx = mover.simpleMove(minx, "U")
                case "D--": minx = mover.simpleMove(minx, "D--")
                case "D++": minx = mover.simpleMove(minx, "D++")
                case "R--": minx = mover.simpleMove(minx, "R--")
                case "R++": minx = mover.simpleMove(minx, "R++")
        return minx
    
    def getScrambledMegaminx(self, mv, minx):
        randomScramble = self.scrambleList[randint(0,len(self.scrambleList)-1)]
        return MegaminxScrambler.scrambleMegaminx(minx, mv, randomScramble)