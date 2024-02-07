""" abs moves """
from megaminx import Megaminx
from moves.utils import FaceUtils

def move_AL(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.rotate(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    dl[6], dl[7], dl[8] = minx.left[6], minx.left[7], minx.left[8]
    l[6], l[7], l[8] = minx.backLeft[4], minx.backLeft[5], minx.backLeft[6]
    d[6], d[7], d[8] = minx.downLeft[6], minx.downLeft[7], minx.downLeft[8]
    bl[4], bl[5], bl[6] = minx.back[2], minx.back[3], minx.back[4]
    b[2], b[3], b[4] = minx.down[6], minx.down[7], minx.down[8]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_AL_prime(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.rotateAsync(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    dl[6], dl[7], dl[8] = minx.down[6], minx.down[7], minx.down[8]
    l[6], l[7], l[8] = minx.downLeft[6], minx.downLeft[7], minx.downLeft[8]
    d[6], d[7], d[8] = minx.back[2], minx.back[3], minx.back[4]
    bl[4], bl[5], bl[6] = minx.left[6], minx.left[7], minx.left[8]
    b[2], b[3], b[4] = minx.backLeft[4], minx.backLeft[5], minx.backLeft[6]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_AL2(minx):
    m = move_AL(minx)
    return move_AL(m)

def move_AL3(minx):
    m = move_AL2(minx)
    return move_AL(m)

def move_AL2_prime(minx):
    m = move_AL_prime(minx)
    return move_AL_prime(m)

def move_AL3_prime(minx):
    m = move_AL2_prime(minx)
    return move_AL_prime(m)

def move_AR(minx):
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
    ar = FaceUtils.rotate(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    dr[2], dr[3], dr[4] = minx.down[2], minx.down[3], minx.down[4]
    r[4], r[5], r[6] = minx.downRight[2], minx.downRight[3], minx.downRight[4]
    br[6], br[7], br[8] = minx.right[4], minx.right[5], minx.right[6]
    d[2], d[3], d[4] = minx.back[6], minx.back[7], minx.back[8]
    b[6], b[7], b[8] = minx.backRight[6], minx.backRight[7], minx.backRight[8]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_AR_prime(minx):
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
    ar = FaceUtils.rotateAsync(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    dr[2], dr[3], dr[4] = minx.right[4], minx.right[5], minx.right[6]
    r[4], r[5], r[6] = minx.backRight[6], minx.backRight[7], minx.backRight[8]
    br[6], br[7], br[8] = minx.back[6], minx.back[7], minx.back[8]
    d[2], d[3], d[4] = minx.downRight[2], minx.downRight[3], minx.downRight[4]
    b[6], b[7], b[8] = minx.down[2], minx.down[3], minx.down[4]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_AR2(minx):
    m = move_AR(minx)
    return move_AR(m)

def move_AR3(minx):
    m = move_AR2(minx)
    return move_AR(m)

def move_AR2_prime(minx):
    m = move_AR_prime(minx)
    return move_AR_prime(m)

def move_AR3_prime(minx):
    m = move_AR2_prime(minx)
    return move_AR_prime(m)
