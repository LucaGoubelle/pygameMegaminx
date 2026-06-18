""" utils """

class FaceUtils:
    """ face utils """

    @staticmethod
    def gen_empty_face() -> list[str]:
        return ["" for _ in range(11)]
    
    @staticmethod
    def rotate(face) -> list[str]:
        nf = FaceUtils.gen_empty_face()
        
        nf[0] = face[8]
        nf[1] = face[9]
        nf[2] = face[0]
        nf[3] = face[1]
        nf[4] = face[2]
        
        nf[5] = face[3]
        nf[6] = face[4]
        nf[7] = face[5]
        nf[8] = face[6]
        nf[9] = face[7]
        nf[10] = face[10]
        
        return nf
    
    @staticmethod
    def rotateAsync(face) -> list[str]:
        nf = FaceUtils.gen_empty_face()
        
        nf[0] = face[2]
        nf[1] = face[3]
        nf[2] = face[4]
        nf[3] = face[5]
        nf[4] = face[6]
        
        nf[5] = face[7]
        nf[6] = face[8]
        nf[7] = face[9]
        nf[8] = face[0]
        nf[9] = face[1]
        nf[10] = face[10]
        
        return nf
    
    @staticmethod
    def rotateTwice(face) -> list[str]:
        nf = FaceUtils.rotate(face)
        return FaceUtils.rotate(nf)
    
    @staticmethod
    def rotateTwiceAsync(face) -> list[str]:
        nf = FaceUtils.rotateAsync(face)
        return FaceUtils.rotateAsync(nf)
    
    @staticmethod
    def rotateThree(face) -> list[str]:
        nf = FaceUtils.rotate(face)
        nff = FaceUtils.rotate(nf)
        return FaceUtils.rotate(nff)
    
    @staticmethod
    def rotateThreeAsync(face) -> list[str]:
        nf = FaceUtils.rotateAsync(face)
        nff = FaceUtils.rotateAsync(nf)
        return FaceUtils.rotateAsync(nff)

    @staticmethod
    def transfert(face) -> list[str]:
        nf = FaceUtils.gen_empty_face()
        for i in range(len(face)):
            nf[i] = face[i]
        return nf
