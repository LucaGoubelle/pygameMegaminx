""" megaminx data model """

class Megaminx:
    """ megaminx data model """
    
    def __init__(self, **kwargs):
        if kwargs["full"] == True:
            self.up = ["gray" for _ in range(11)]
            self.front = ["magenta" for _ in range(11)]
            self.left = ["green" for _ in range(11)]
            self.right = ["beige" for _ in range(11)]
            self.downRight = ["red" for _ in range(11)]
            self.downLeft = ["blue" for _ in range(11)]
            self.absLeft = ["yellow" for _ in range(11)]
            self.absRight = ["green4" for _ in range(11)]
            self.down = ["white" for _ in range(11)]
            self.backLeft = ["orange" for _ in range(11)]
            self.backRight = ["cyan" for _ in range(11)]
            self.back = ["purple" for _ in range(11)]
        else:
            self.up = kwargs["up"]
            self.front = kwargs["front"]
            self.left = kwargs["left"]
            self.right = kwargs["right"]
            self.downRight = kwargs["downRight"]
            self.downLeft = kwargs["downLeft"]
            self.absLeft = kwargs["absLeft"]
            self.absRight = kwargs["absRight"]
            self.down = kwargs["down"]
            self.backLeft = kwargs["backLeft"]
            self.backRight = kwargs["backRight"]
            self.back = kwargs["back"]
