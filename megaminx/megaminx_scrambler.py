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
    
    def scrambleMegaminx(self, minx, mover, scramble):
        scrambleLst = scramble.split()
        for mv in scrambleLst:
            minx = mover.simpleMove(minx, mv)
        return minx
    
    def getScrambledMegaminx(self, mv, minx):
        rand: int = randint(0,len(self.scrambleList)-1)
        randomScramble = self.scrambleList[rand]
        return self.scrambleMegaminx(minx, mv, randomScramble)
