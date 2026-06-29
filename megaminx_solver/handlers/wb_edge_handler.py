""" WHITE BLUE edge handler """
from megaminx_solver.handlers.handler import Handler
from megaminx_solver.helpers.edge_finder import EdgeFinder


class WBEdgeHandler(Handler):
    """ WB Edge handler """
    
    def __init__(self, mover):
        super().__init__(mover)
        self.edge_finder = EdgeFinder()
        # TODO: add cases
        self.cases = {
            "up_front::white_blue": "",
            "up_left::white_blue": "y'",
            "up_right::white_blue": "y",
            "up_backLeft::white_blue": "y2'",
            "up_backRight::white_blue": "y2",
        }
        
    def handle_wb_edge(self, minx):
        result_finder = self.edge_finder.find(minx, ["white","blue"])
        results: str = f"{result_finder['orients']}::{result_finder['colors']}"
        sequence = self.cases[results] if results in self.cases else ""
        minx = self.mover.multiMove(minx, sequence)
        return minx
