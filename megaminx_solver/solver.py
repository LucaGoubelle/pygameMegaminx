""" megaminx solver """
from megaminx_solver.handlers.start_handler import StartHandler


class MegaminxSolver:
    """ megaminx solver """

    def __init__(self, mover):
        self.start_handler = StartHandler(mover)

    def solve(self, minx):
        """ solve megaminx """
        minx = self.start_handler.handle_start(minx)
        # todo: implement remaining lines
        return minx
