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
    
    def scrambleMegaminx(minx, mv, scramble):
        scrambleLst = MegaminxScrambler.getAllMoves(scramble)
        for mv in scrambleLst:
            match mv:
                case "U": minx = mv.simpleMove(minx, "U")
                case "U'": minx = mv.simpleMove(minx, "U")
                case "D--": minx = mv.simpleMove(minx, "D--")
                case "D++": minx = mv.simpleMove(minx, "D++")
                case "R--": minx = mv.simpleMove(minx, "R--")
                case "R++": minx = mv.simpleMove(minx, "R++")
        return minx
    
    def getScrambledMegaminx(self, minx):
        randomScramble = self.scrambleList[randint(0,len(self.scrambleList)-1)]
        return MegaminxScrambler.scrambleMegaminx(minx, randomScramble)