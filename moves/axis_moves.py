""" axis moves """
from megaminx import Megaminx
from moves.utils import FaceUtils

# --------- Y -------------------

def move_y(minx):
    u = FaceUtils.rotate(minx.up)
    f = FaceUtils.transfert(minx.right)
    l = FaceUtils.transfert(minx.front)
    r = FaceUtils.transfert(minx.backRight)
    bl = FaceUtils.transfert(minx.left)
    br = FaceUtils.transfert(minx.backLeft)
    d = FaceUtils.rotateAsync(minx.down)
    dl = FaceUtils.transfert(minx.downRight)
    dr = FaceUtils.transfert(minx.absRight)
    al = FaceUtils.transfert(minx.downLeft)
    ar = FaceUtils.transfert(minx.back)
    b = FaceUtils.transfert(minx.absLeft)
    
    return Megaminx(
        full="no", 
        up=u, front=f, left=l, right=r, 
        backLeft=bl, backRight=br,
        down=d, downLeft=dl, downRight=dr,
        absLeft=al, absRight=ar, back=b
    )

def move_y_prime(minx):
    u = FaceUtils.rotateAsync(minx.up)
    f = FaceUtils.transfert(minx.left)
    l = FaceUtils.transfert(minx.backLeft)
    r = FaceUtils.transfert(minx.front)
    bl = FaceUtils.transfert(minx.backRight)
    br = FaceUtils.transfert(minx.right)
    d = FaceUtils.rotate(minx.down)
    dl = FaceUtils.transfert(minx.absLeft)
    dr = FaceUtils.transfert(minx.downLeft)
    al = FaceUtils.transfert(minx.back)
    ar = FaceUtils.transfert(minx.downRight)
    b = FaceUtils.transfert(minx.absRight)
    
    return Megaminx(
        full="no", 
        up=u, front=f, left=l, right=r, 
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar,back=b
    )
    
def move_y2(minx):
    m = move_y(minx)
    return move_y(m)
    
def move_y2_prime(minx):
    m = move_y_prime(minx)
    return move_y_prime(m)

def move_y3(minx):
    m = move_y2(minx)
    return move_y(m)

def move_y3_prime(minx):
    m = move_y2_prime(minx)
    return move_y_prime(m)

# --------------------- Z -------------------------------

def move_z(minx):
    u = FaceUtils.rotate(minx.left)
    f = FaceUtils.rotate(minx.front)
    l = FaceUtils.rotate(minx.downLeft)
    r = FaceUtils.rotateTwice(minx.up)
    bl = FaceUtils.transfert(minx.absLeft)
    br = FaceUtils.rotateAsync(minx.backLeft)
    d = FaceUtils.rotate(minx.absRight)
    dl = FaceUtils.rotate(minx.downRight)
    dr = FaceUtils.transfert(minx.right)
    al = FaceUtils.rotate(minx.down)
    ar = FaceUtils.rotateAsync(minx.backRight)
    b = FaceUtils.rotateAsync(minx.back)

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_z_prime(minx):
    u = FaceUtils.rotateTwiceAsync(minx.right)
    f = FaceUtils.rotateAsync(minx.front)
    l =  FaceUtils.rotateAsync(minx.up)
    r = FaceUtils.transfert(minx.downRight)
    bl = FaceUtils.rotate(minx.backRight)
    br = FaceUtils.rotate(minx.absRight)
    d = FaceUtils.rotateAsync(minx.absLeft)
    dl = FaceUtils.rotateAsync(minx.left)
    dr = FaceUtils.rotateAsync(minx.downLeft)
    al = FaceUtils.transfert(minx.backLeft)
    ar = FaceUtils.rotateAsync(minx.down)
    b = FaceUtils.rotate(minx.back)

    return Megaminx(
        full="no",
        up=u,front=f,left=l,right=r,
        backLeft=bl,backRight=br,
        down=d,downLeft=dl,downRight=dr,
        absLeft=al,absRight=ar, back=b
    )

def move_z2(minx):
    m = move_z(minx)
    return move_z(m)

def move_z2_prime(minx):
    m = move_z_prime(minx)
    return move_z_prime(m)

def move_z3(minx):
    m = move_z2(minx)
    return move_z(m)

def move_z3_prime(minx):
    m = move_z2_prime(minx)
    return move_y_prime(m)

