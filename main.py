modulo = 709
px = 266
py = 232
q = 113
qx = 121
qy = 247
tx = 603
ty = 607


a = 37
m = 24
mxg = []
myg = []
answer = 0

def inverse(x):
    return x**(modulo-2)

def equal(px, py):
    l1 = (3 * px ** 2 + a) * inverse(2 * py)
    x3 = l1** 2 - px - px
    y3 = -py + l1 * (px - x3)
    qx = x3 % modulo
    qy = y3 % modulo
    return qx, qy

def different(px, py, qx, qy):
    l2 = (py - qy) * inverse(px - qx)
    x3 = l2**2 - px - qx
    y3 = -py + l2 * (px - x3)
    qx = x3 % modulo
    qy = y3 % modulo
    return qx, qy

def helpfunction(tx, ty):
    if tx % 3 == 0:
        print(0)
        tx, ty = equal(tx, ty)
    elif tx % 3 == 1:
        print(1)
        tx, ty = different(tx, ty, px, py)
    else:
        print(2)
        tx, ty = different(tx, ty, qx, qy)
    return tx, ty



# #print(0, 0, 0)
# mxg.append(0)
# myg.append(0)
# #print(px, py, 1)
# mxg.append(px)
# myg.append(py)
#
# for i in range(m-1):
#     if(px==qx and py==qy):
#         qx, qy = equal(px, py)
#         mxg.append(qx)
#         myg.append(qy)
#         #print(qx, qy, i+2)
#     else:
#         qx, qy = different(px, py, qx, qy)
#         mxg.append(qx)
#         myg.append(qy)
#         #print(qx, qy, i+2)
# #print(ax, ay, 0)
# for j in range(m-1):
#     ax, ay = different(ax, ay, mxg[18], -myg[18])
#     #print(ax, ay, j+1)
#     for i in range(len(mxg)):
#         if mxg[i] == ax and myg[i] == ay:
#             answer = i+(m*(j+1))
#
#     if answer != 0:
#         break
# #print(answer)

for i in range(20):
    tx, ty = helpfunction(tx, ty)
    print(tx, ty, i+1)