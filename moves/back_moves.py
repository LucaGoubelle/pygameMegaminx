""" back moves """
from megaminx import Megaminx
from moves.utils import FaceUtils

def move_BL(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.rotate(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    u[8], u[9], u[0] = minx.backRight[2], minx.backRight[3], minx.backRight[4]
    l[8], l[9], l[0] = minx.up[8], minx.up[9], minx.up[0]
    br[2], br[3], br[4] = minx.back[0], minx.back[1], minx.back[2]
    b[0], b[1], b[2] = minx.absLeft[8], minx.absLeft[9], minx.absLeft[0]
    al[8], al[9], al[0] = minx.left[8], minx.left[9], minx.left[0]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_BL_prime(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.rotateAsync(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    u[8], u[9], u[0] = minx.left[8], minx.left[9], minx.left[0]
    l[8], l[9], l[0] = minx.absLeft[8], minx.absLeft[9], minx.absLeft[0]
    br[2], br[3], br[4] = minx.up[8], minx.up[9], minx.up[0]
    b[0], b[1], b[2] = minx.backRight[2], minx.backRight[3], minx.backRight[4]
    al[8], al[9], al[0] = minx.back[0], minx.back[1], minx.back[2]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_BL2(minx):
    m = move_BL(minx)
    return move_BL(m)

def move_BL3(minx):
    m = move_BL2(minx)
    return move_BL(m)

def move_BL2_prime(minx):
    m = move_BL_prime(minx)
    return move_BL_prime(m)

def move_BL3_prime(minx):
    m = move_BL2_prime(minx)
    return move_BL_prime(m)

def move_BR(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.rotate(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    u[0], u[1], u[2] = minx.right[2], minx.right[3], minx.right[4]
    r[2], r[3], r[4] = minx.absRight[0], minx.absRight[1], minx.absRight[2]
    bl[8], bl[9], bl[0] = minx.up[0], minx.up[1], minx.up[2]
    b[8], b[9], b[0] = minx.backLeft[8], minx.backLeft[9], minx.backLeft[0]
    ar[0], ar[1], ar[2] = minx.back[8], minx.back[9], minx.back[0]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_BR_prime(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.rotateAsync(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    u[0], u[1], u[2] = minx.backLeft[8], minx.backLeft[9], minx.backLeft[0]
    r[2], r[3], r[4] = minx.up[0], minx.up[1], minx.up[2]
    bl[8], bl[9], bl[0] = minx.back[8], minx.back[9], minx.back[0]
    b[8], b[9], b[0] = minx.absRight[0], minx.absRight[1], minx.absRight[2]
    ar[0], ar[1], ar[2] = minx.right[2], minx.right[3], minx.right[4]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_BR2(minx):
    m = move_BR(minx)
    return move_BR(m)

def move_BR3(minx):
    m = move_BR2(minx)
    return move_BR(m)

def move_BR2_prime(minx):
    m = move_BR_prime(minx)
    return move_BR_prime(m)

def move_BR3_prime(minx):
    m = move_BR2_prime(minx)
    return move_BR_prime(m)

