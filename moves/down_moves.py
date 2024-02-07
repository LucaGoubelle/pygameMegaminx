""" down moves """
from megaminx import Megaminx
from moves.utils import FaceUtils

def move_DL(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.rotate(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    l[4], l[5], l[6] = minx.absLeft[2], minx.absLeft[3], minx.absLeft[4]
    f[6], f[7], f[8] = minx.left[4], minx.left[5], minx.left[6]
    dr[6], dr[7], dr[8] = minx.front[6], minx.front[7], minx.front[8]
    d[0], d[9], d[8] = minx.downRight[8], minx.downRight[7], minx.downRight[6]
    al[2], al[3], al[4] = minx.down[8], minx.down[9], minx.down[0]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_DL_prime(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.rotateAsync(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    l[4], l[5], l[6] = minx.front[6], minx.front[7], minx.front[8]
    f[6], f[7], f[8] = minx.downRight[6], minx.downRight[7], minx.downRight[8]
    dr[6], dr[7], dr[8] = minx.down[8], minx.down[9], minx.down[0]
    d[0], d[9], d[8] = minx.absLeft[4], minx.absLeft[3], minx.absLeft[2]
    al[2], al[3], al[4] = minx.left[4], minx.left[5], minx.left[6]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_DL2(minx):
    m = move_DL(minx)
    return move_DL(m)

def move_DL3(minx):
    m = move_DL2(minx)
    return move_DL(m)

def move_DL2_prime(minx):
    m = move_DL_prime(minx)
    return move_DL_prime(m)

def move_DL3_prime(minx):
    m = move_DL2_prime(minx)
    return move_DL_prime(m)

def move_DR(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.rotate(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    f[4], f[5], f[6] = minx.downLeft[2], minx.downLeft[3], minx.downLeft[4]
    r[6], r[7], r[8] = minx.front[4], minx.front[5], minx.front[6]
    dl[2], dl[3], dl[4] = minx.down[0], minx.down[1], minx.down[2]
    ar[6], ar[7], ar[8] = minx.right[6], minx.right[7], minx.right[8]
    d[0], d[1], d[2] = minx.absRight[6], minx.absRight[7], minx.absRight[8]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_DR_prime(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.rotateAsync(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    f[4], f[5], f[6] = minx.right[6], minx.right[7], minx.right[8]
    r[6], r[7], r[8] = minx.absRight[6], minx.absRight[7], minx.absRight[8]
    dl[2], dl[3], dl[4] = minx.front[4], minx.front[5], minx.front[6]
    ar[6], ar[7], ar[8] = minx.down[0], minx.down[1], minx.down[2]
    d[0], d[1], d[2] = minx.downLeft[2], minx.downLeft[3], minx.downLeft[4]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_DR2(minx):
    m = move_DR(minx)
    return move_DR(m)

def move_DR3(minx):
    m = move_DR2(minx)
    return move_DR(m)

def move_DR2_prime(minx):
    m = move_DR_prime(minx)
    return move_DR_prime(m)

def move_DR3_prime(minx):
    m = move_DR2_prime(minx)
    return move_DR_prime(m)

def move_D(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.rotate(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    dl[4], dl[5], dl[6] = minx.absLeft[4], minx.absLeft[5], minx.absLeft[6]
    dr[4], dr[5], dr[6] = minx.downLeft[4], minx.downLeft[5], minx.downLeft[6]
    ar[4], ar[5], ar[6] = minx.downRight[4], minx.downRight[5], minx.downRight[6]
    al[4], al[5], al[6] = minx.back[4], minx.back[5], minx.back[6]
    b[4], b[5], b[6] = minx.absRight[4], minx.absRight[5], minx.absRight[6]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_D_prime(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.rotateAsync(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    dl[4], dl[5], dl[6] = minx.downRight[4], minx.downRight[5], minx.downRight[6]
    dr[4], dr[5], dr[6] = minx.absRight[4], minx.absRight[5], minx.absRight[6]
    ar[4], ar[5], ar[6] = minx.back[4], minx.back[5], minx.back[6]
    al[4], al[5], al[6] = minx.downLeft[4], minx.downLeft[5], minx.downLeft[6]
    b[4], b[5], b[6] = minx.absLeft[4], minx.absLeft[5], minx.absLeft[6]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_D2(minx):
    m = move_D(minx)
    return move_D(m)

def move_D3(minx):
    m = move_D2(minx)
    return move_D(m)

def move_D2_prime(minx):
    m = move_D_prime(minx)
    return move_D_prime(m)

def move_D3_prime(minx):
    m = move_D2_prime(minx)
    return move_D_prime(m)
