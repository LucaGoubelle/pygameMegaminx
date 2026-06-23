""" edge finder """

class EdgeFinder:
    """ edge finder """
    
    def find(self, minx, colors: list[str]) -> dict[str, str]:
        """
        find an edge of specified colors on specified minx puzzle,
        return : dictionary of two vals :
        - orients string
        - colors string
        """
        # TODO: test it in handler (solver)
        result_orient: str = "???"
        result_colors: str = "???"
        case_1: str = f"{colors[0]}_{colors[1]}"
        case_2: str = f"{colors[1]}_{colors[0]}"
        hmap = {
            "up_front": minx.up[5]+"_"+minx.front[1],
            "up_left": minx.up[7]+"_"+minx.left[1],
            "up_right": minx.up[3]+"_"+minx.right[1],
            "up_backLeft": minx.up[9]+"_"+minx.backLeft[1],
            "up_backRight": minx.up[1]+"_"+minx.backRight[1],
            
            "front_left": minx.front[9]+"_"+minx.left[3],
            "front_right": minx.front[3]+"_"+minx.right[9],
            "backLeft_backRight": minx.backLeft[9]+"_"+minx.backRight[3],
            "backLeft_left": minx.backLeft[3]+"_"+minx.left[9],
            "backRight_right": minx.backRight[9]+"_"+minx.right[3],
            
            "front_downLeft": minx.front[7]+"_"+minx.downLeft[1],
            "front_downRight": minx.front[5]+"_"+minx.downRight[9],
            
            "downLeft_left": minx.downLeft[9]+"_"+minx.left[5],
            "downRight_right": minx.downRight[1]+"_"+minx.right[7],
            
            "absLeft_left": minx.absLeft[1]+"_"+minx.left[7],
            "absRight_right": minx.absRight[9]+"_"+minx.right[5],
            
            "backLeft_absLeft": minx.backLeft[5]+"_"+minx.absLeft[9],
            "backRight_absRight": minx.backRight[7]+"_"+minx.absRight[1],
            
            "back_backLeft": minx.back[1]+"_"+minx.backLeft[7],
            "back_backRight": minx.back[9]+"_"+minx.backRight[5],
            
            "downLeft_downRight": minx.downLeft[3]+"_"+minx.downRight[7],
            "downLeft_absLeft": minx.downLeft[7]+"_"+minx.absLeft[3],
            "downRight_absRight": minx.downRight[3]+"_"+minx.absRight[7],
            "back_absLeft": minx.back[3]+"_"+minx.absLeft[7],
            "back_absRight": minx.back[7]+"_"+minx.absRight[3],
            
            "down_downLeft": minx.down[9]+"_"+minx.downLeft[5],
            "down_downRight": minx.down[1]+"_"+minx.downRight[5],
            "down_absRight": minx.down[3]+"_"+minx.absRight[5],
            "down_absLeft": minx.down[7]+"_"+minx.absLeft[5],
            "down_back": minx.down[5]+"_"+minx.back[5]
        }
        for k,v in hmap.items():
            if v == case_1 or v == case_2:
                result_colors = v
                result_orient = k
                break
        return {
            "orients": result_orient, 
            "colors": result_colors
        }
