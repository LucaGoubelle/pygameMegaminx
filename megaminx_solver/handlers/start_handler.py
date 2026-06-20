""" start handler """
from megaminx_solver.handlers.handler import Handler

class StartHandler(Handler):
    """ start handler """

    def __init__(self, mover):
        super().__init__(mover)
        # todo: implement other cases
        self.cases = {
            "white_blue_red": "",
            "white_red_green": "y",
            "white_green_purple": "y2",
            "white_purple_yellow": "y2'",
            "white_yellow_blue": "y'",

            "gray_magenta_lime": "z y' z2",
            "gray_lime_orange": "z y' z2 y'",
            "gray_orange_cyan": "z y' z2 y2'",
            "gray_cyan_beige": "z y' z2 y2",
            "gray_beige_magenta": "z y' z2 y"
        }
    
    def handle_start(self, minx):
        """ handle start (orienting) """
        center_up = minx.up[10]
        center_front = minx.front[10]
        center_left = minx.left[10]
        colors = "_".join([center_up, center_front, center_left])
        minx = self.mover.multiMove(minx, self.cases[colors])
        return minx
