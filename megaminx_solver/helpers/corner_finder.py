""" corner finder """

class CornerFinder:
    """ corner finder """
    
    def find(self, minx, colors: list[str]) -> dict[str, str]:
        """
        find a corner of specified colors on specified minx puzzle,
        return : dictionary of two vals :
        - orients string
        - colors string
        """
        # TODO: test it in handler (solver)
        result_orient: str = "???"
        result_colors: str = "???"
        cases = [
            f"{colors[0]}_{colors[1]}_{colors[2]}", 
            f"{colors[0]}_{colors[2]}_{colors[1]}", 
            f"{colors[1]}_{colors[0]}_{colors[2]}",
            f"{colors[1]}_{colors[2]}_{colors[0]}", 
            f"{colors[2]}_{colors[0]}_{colors[1]}", 
            f"{colors[2]}_{colors[1]}_{colors[0]}"
        ]
        #TODO: add other cases...
        hmap = {
            "up_front_left": f"{minx.up[6]}_{minx.front[0]}_{minx.left[2]}",
            "up_front_right": f"{minx.up[4]}_{minx.front[2]}_{minx.right[0]}",
            "up_backLeft_left": f"{minx.up[8]}_{minx.backLeft[2]}_{minx.left[0]}",
            "up_backRight_right": f"{minx.up[2]}_{minx.backRight[0]}_{minx.right[2]}",
            "up_backLeft_backRight": f"{minx.up[0]}_{minx.backLeft[0]}_{minx.backRight[2]}",
            
            "front_downLeft_downRight": f"{minx.front[6]}_{minx.downLeft[2]}_{minx.downRight[8]}",
            "front_downLeft_left": f"{minx.front[8]}_{minx.downLeft[0]}_{minx.left[4]}",
            "front_downRight_right": f"{minx.front[4]}_{minx.downRight[0]}_{minx.right[8]}",
            
            "down_downLeft_downRight": f"{minx.down[0]}_{minx.downLeft[4]}_{minx.downRight[6]}",
            "down_downLeft_absLeft": f"{minx.down[8]}_{minx.downLeft[6]}_{minx.absLeft[4]}",
            "down_downRight_absRight": f"{minx.down[2]}_{minx.downRight[4]}_{minx.absRight[6]}",
            "down_back_absLeft": f"{minx.down[6]}_{minx.back[4]}_{minx.absLeft[6]}",
            "down_back_absRight": f"{minx.down[4]}_{minx.back[6]}_{minx.absRight[4]}",
        }
        for k,v in hmap.items():
            if v in cases:
                result_colors = v
                result_orient = k
                break
        return {
            "orients": result_orient,
            "colors": result_colors
        }
