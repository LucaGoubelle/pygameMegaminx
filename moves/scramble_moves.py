""" scramble moves """
from megaminx import Megaminx
from moves.utils import FaceUtils

def move_RPP(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    u[9], u[0], u[1], u[2], u[3], u[4], u[5], u[10] = minx.downLeft[1], minx.downLeft[2], minx.downLeft[3], minx.downLeft[4], minx.downLeft[5], minx.downLeft[6], minx.downLeft[7], minx.downLeft[10]
    f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[10] = minx.absLeft[3], minx.absLeft[4], minx.absLeft[5], minx.absLeft[6], minx.absLeft[7], minx.absLeft[8], minx.absLeft[9], minx.absLeft[10]
    r = FaceUtils.rotate(minx.down)
    bl[5], bl[6], bl[7], bl[8], bl[9], bl[0], bl[1], bl[10] = minx.front[1], minx.front[2], minx.front[3], minx.front[4], minx.front[5], minx.front[6], minx.front[7], minx.front[10]
    br = FaceUtils.rotateTwice(minx.downRight)
    d = FaceUtils.rotateTwiceAsync(minx.backRight)
    dl[1], dl[2], dl[3], dl[4], dl[5], dl[6], dl[7], dl[10] = minx.backLeft[5], minx.backLeft[6], minx.backLeft[7], minx.backLeft[8], minx.backLeft[9], minx.backLeft[0], minx.backLeft[1], minx.backLeft[10]
    dr = FaceUtils.rotateTwiceAsync(minx.back)
    al[3], al[4], al[5], al[6], al[7], al[8], al[9], al[10] = minx.up[9], minx.up[0], minx.up[1], minx.up[2], minx.up[3], minx.up[4], minx.up[5], minx.up[10]
    ar = FaceUtils.rotateTwice(minx.absRight)
    b = FaceUtils.rotate(minx.right)

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )
    
def move_RMM(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    u[9], u[0], u[1], u[2], u[3], u[4], u[5], u[10] = minx.absLeft[3], minx.absLeft[4], minx.absLeft[5], minx.absLeft[6], minx.absLeft[7], minx.absLeft[8], minx.absLeft[9], minx.absLeft[10]
    f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[10] = minx.backLeft[5], minx.backLeft[6], minx.backLeft[7], minx.backLeft[8], minx.backLeft[9], minx.backLeft[0], minx.backLeft[1], minx.backLeft[10]
    r = FaceUtils.rotateAsync(minx.back)
    bl[5], bl[6], bl[7], bl[8], bl[9], bl[0], bl[1], bl[10] = minx.downLeft[1], minx.downLeft[2], minx.downLeft[3], minx.downLeft[4], minx.downLeft[5], minx.downLeft[6], minx.downLeft[7], minx.downLeft[10]
    br = FaceUtils.rotateTwice(minx.down)
    d = FaceUtils.rotateAsync(minx.right)
    dl[1], dl[2], dl[3], dl[4], dl[5], dl[6], dl[7], dl[10] = minx.up[9], minx.up[0], minx.up[1], minx.up[2], minx.up[3], minx.up[4], minx.up[5], minx.up[10]
    dr = FaceUtils.rotateTwiceAsync(minx.backRight)
    al[3], al[4], al[5], al[6], al[7], al[8], al[9], al[10] = minx.front[1], minx.front[2], minx.front[3], minx.front[4], minx.front[5], minx.front[6], minx.front[7], minx.front[10]
    ar = FaceUtils.rotateTwiceAsync(minx.absRight)
    b = FaceUtils.rotateTwice(minx.downRight)

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_DPP(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    for i in range(3,11,1):
        f[i] = minx.backLeft[i]
        l[i] = minx.backRight[i]
        r[i] = minx.left[i]
        bl[i] = minx.right[i]
        br[i] = minx.front[i]
    
    d = FaceUtils.rotateTwice(minx.down)
    dl = FaceUtils.transfert(minx.back)
    dr = FaceUtils.transfert(minx.absLeft)
    al = FaceUtils.transfert(minx.absRight)
    ar = FaceUtils.transfert(minx.downLeft)
    b = FaceUtils.transfert(minx.downRight)

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_DMM(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    for i in range(3,11,1):
        f[i] = minx.backRight[i]
        l[i] = minx.right[i]
        r[i] = minx.backLeft[i]
        bl[i] = minx.front[i]
        br[i] = minx.left[i]
    
    d = FaceUtils.rotateTwiceAsync(minx.down)
    dl = FaceUtils.transfert(minx.absRight)
    dr = FaceUtils.transfert(minx.back)
    al = FaceUtils.transfert(minx.downRight)
    ar = FaceUtils.transfert(minx.absLeft)
    b = FaceUtils.transfert(minx.downLeft)

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )
