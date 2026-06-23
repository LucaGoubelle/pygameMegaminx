""" WHITE BLUE edge handler """
from megaminx_solver.handlers.handler import Handler


class WBEdgeHandler(Handler):
    """ WB Edge handler """
    
    def __init__(self, mover):
        super().__init__(mover)
        self.cases = {}
        
    def handle_wb_edge(self, minx):
        # TODO: implement this
        # TODO: + add edge finder
        return minx
