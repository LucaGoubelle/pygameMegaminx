""" std moves """
from megaminx import Megaminx
from moves.utils import FaceUtils

def move_U(minx):
    u = FaceUtils.rotate(minx.up)
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

    for i in range(3):
        f[i] = minx.right[i]
        l[i] = minx.front[i]
        r[i] = minx.backRight[i]
        bl[i] = minx.left[i]
        br[i] = minx.backLeft[i]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_U_prime(minx):
    u = FaceUtils.rotateAsync(minx.up)
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

    for i in range(3):
        f[i] = minx.left[i]
        l[i] = minx.backLeft[i]
        r[i] = minx.front[i]
        bl[i] = minx.backRight[i]
        br[i] = minx.right[i]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_U2(minx):
    m = move_U(minx)
    return move_U(m)

def move_U3(minx):
    m = move_U2(minx)
    return move_U(m)

def move_U2_prime(minx):
    m = move_U_prime(minx)
    return move_U_prime(m)

def move_U3_prime(minx):
    m = move_U2_prime(minx)
    return move_U_prime(m)   

def move_R(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.rotate(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    for i in range(2,5,1):
        u[i] = minx.front[i]
    
    f[2], f[3], f[4] = minx.downRight[0], minx.downRight[1], minx.downRight[2]
    dr[0], dr[1], dr[2] = minx.absRight[8], minx.absRight[9], minx.absRight[0]
    ar[8], ar[9], ar[0] = minx.backRight[8], minx.backRight[9], minx.backRight[0]
    br[8], br[9], br[0] = minx.up[2], minx.up[3], minx.up[4]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_R_prime(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.transfert(minx.left)
    r = FaceUtils.rotateAsync(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    u[2], u[3], u[4] = minx.backRight[8], minx.backRight[9], minx.backRight[0]
    f[2], f[3], f[4] = minx.up[2], minx.up[3], minx.up[4]
    dr[0], dr[1], dr[2] = minx.front[2], minx.front[3], minx.front[4]
    ar[8], ar[9], ar[0] = minx.downRight[0], minx.downRight[1], minx.downRight[2]
    br[8], br[9], br[0] = minx.absRight[8], minx.absRight[9], minx.absRight[0]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )


def move_R2(minx):
    m = move_R(minx)
    return move_R(m)

def move_R3(minx):
    m = move_R2(minx)
    return move_R(m)

def move_R2_prime(minx):
    m = move_R_prime(minx)
    return move_R_prime(m)

def move_R3_prime(minx):
    m = move_R2_prime(minx)
    return move_R_prime(m)

def move_L(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.rotate(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    u[8], u[7], u[6] = minx.backLeft[4], minx.backLeft[3], minx.backLeft[2]
    f[0], f[9], f[8] = minx.up[8], minx.up[7], minx.up[6]
    dl[0], dl[9], dl[8] = minx.front[0], minx.front[9], minx.front[8]
    al[0], al[1], al[2] = minx.downLeft[8], minx.downLeft[9], minx.downLeft[0]
    bl[2], bl[3], bl[4] = minx.absLeft[0], minx.absLeft[1], minx.absLeft[2]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_L_prime(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.transfert(minx.front)
    l = FaceUtils.rotateAsync(minx.left)
    r = FaceUtils.transfert(minx.right)
    bl = FaceUtils.transfert(minx.backLeft)
    br = FaceUtils.transfert(minx.backRight)
    d = FaceUtils.transfert(minx.down)
    dl = FaceUtils.transfert(minx.downLeft)
    dr = FaceUtils.transfert(minx.downRight)
    al = FaceUtils.transfert(minx.absLeft)
    ar = FaceUtils.transfert(minx.absRight)
    b = FaceUtils.transfert(minx.back)

    u[8], u[7], u[6] = minx.front[0], minx.front[9], minx.front[8]
    f[0], f[9], f[8] = minx.downLeft[0], minx.downLeft[9], minx.downLeft[8]
    dl[0], dl[9], dl[8] = minx.absLeft[2], minx.absLeft[1], minx.absLeft[0]
    al[0], al[1], al[2] = minx.backLeft[2], minx.backLeft[3], minx.backLeft[4]
    bl[2], bl[3], bl[4] = minx.up[6], minx.up[7], minx.up[8]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_L2(minx):
    m = move_L(minx)
    return move_L(m)

def move_L3(minx):
    m = move_L2(minx)
    return move_L(m)

def move_L2_prime(minx):
    m = move_L_prime(minx)
    return move_L_prime(m)

def move_L3_prime(minx):
    m = move_L2_prime(minx)
    return move_L_prime(m)

def move_F(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.rotate(minx.front)
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

    u[6], u[5], u[4] = minx.left[4], minx.left[3], minx.left[2]
    r[0], r[9], r[8] = minx.up[6], minx.up[5], minx.up[4]
    dr[0], dr[9], dr[8] = minx.right[0], minx.right[9], minx.right[8]
    dl[0], dl[1], dl[2] = minx.downRight[8], minx.downRight[9], minx.downRight[0]
    l[2], l[3], l[4] = minx.downLeft[0], minx.downLeft[1], minx.downLeft[2]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_F_prime(minx):
    u = FaceUtils.transfert(minx.up)
    f = FaceUtils.rotateAsync(minx.front)
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

    u[6], u[5], u[4] = minx.right[0], minx.right[9], minx.right[8]
    r[0], r[9], r[8] = minx.downRight[0], minx.downRight[9], minx.downRight[8]
    dr[0], dr[9], dr[8] = minx.downLeft[2], minx.downLeft[1], minx.downLeft[0]
    dl[0], dl[1], dl[2] = minx.left[2], minx.left[3], minx.left[4]
    l[2], l[3], l[4] = minx.up[4], minx.up[5], minx.up[6]

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_F2(minx):
    m = move_F(minx)
    return move_F(m)

def move_F3(minx):
    m = move_F2(minx)
    return move_F(m)

def move_F2_prime(minx):
    m = move_F_prime(minx)
    return move_F_prime(m)

def move_F3_prime(minx):
    m = move_F2_prime(minx)
    return move_F_prime(m)
