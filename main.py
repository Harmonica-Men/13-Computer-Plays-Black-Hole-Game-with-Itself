import random
import math

flag2 = 0
flag = 0
bcount = 0
numworm = 0
bound = 25
posx = 0
posy = 0
xs = 0
ys = 0
x = [0] * 2000
y = [0] * 2000
dl = 0.0
r = 0.0

random.seed(123456789)  # seed random number generator

bcount = 0
numworm = 0

for numworm in range(1, 1000):
    # randomly select first point of worm
    x[bcount] = bound * random.random()
    y[bcount] = bound * random.random()

    posx = x[bcount - 1]
    posy = y[bcount - 1]

    r = random.random()

    if r <= 0.25:
        posx = posx + 1
    elif 0.25 < r <= 0.5:
        posx = posx - 1
    elif 0.5 < r <= 0.75:
        posy = posy + 1
    elif r > 0.75:
        posy = posy - 1

    # make sure worm does not travel off board
    posx = max(0, posx)
    posy = max(0, posy)
    posx = min(bound, posx)
    posy = min(bound, posy)

    x[bcount] = posx
    y[bcount] = posy
    bcount += 1

flag = 0
bcount -= 1

# scan to make sure worm does not intersect other worms
for i in range(bcount - 5, bcount):
    for j in range(0, bcount - 5):
        if abs(x[i] - x[j]) < 2 and abs(y[i] - y[j]) < 2:
            flag = 1

# scan to make sure worm does not intersect itself
for i in range(bcount - 5, bcount - 1):
    for j in range(i + 1, bcount):
        if x[i] == x[j] and y[i] == y[j]:
            flag = 1


def testdist():
    pass


testdist()

if flag == 0:
    # Print 6 points for plotting the worm body
    for i in range(bcount - 5, bcount):
        print(f"{x[i]} {y[i]}")

    # Print worm head at the following point:
    if flag2 == 0:
        print(f"{x[i - 1]} {y[i - 1]}")
    else:
        print(f"{x[i - 6]} {y[i - 6]}")
else:
    # if flag is not right, the worm intersected others or itself so reset the counter
    bcount = bcount - 5


# Subroutine to determine if worm head is closer to the black hole at the center of the board than the tail
def testdist():
    global flag2

    ex = cy = bound / 2.0  # position black hole in the center
    dl = (x[bcount - 5] - cx) * (x[bcount - 5] - ex) + (y[bcount - 5] - cy) * (y[bcount - 5] - cy)
    d2 = (x[bcount] - cx) * (x[bcount] - ex) + (y[bcount] - cy) * (y[bcount] - cy)

    # flag2 is 0 if the worm points to the hole
    if d2 < dl:
        flag2 = 0
