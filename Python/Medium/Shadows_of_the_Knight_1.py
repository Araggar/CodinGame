import sys
import math

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in raw_input().split()]
n = int(raw_input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in raw_input().split()]
first = True


# game loop
while True:
    bomb_dir = raw_input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if first:
        if bomb_dir in ["DL","UL","L"]:
            w = x0
        else:
            w = w - x0
        if  bomb_dir in ["U","UR","UL"]:
            h = y0
        else:
            h = h - y0
        first = False
    if bomb_dir == "DR":
        x0 = x0 + max(1,w/2.0)
        y0 = y0 + max(1,h/2.0)
        w = w/2.0
        h = h/2.0
    elif bomb_dir == "D":
        y0 = y0 + max(1,h/2.0)
        h = h/2.0
    elif bomb_dir == "R":
        x0 = x0 + max(1,w/2.0)
        w = w/2.0
    elif bomb_dir == "L":
        x0 = x0 - max(1,w/2.0)
        w = w/2.0
    elif bomb_dir == "U":
        y0 = y0 - max(1,h/2.0)
        h = h/2.0    
    elif bomb_dir == "DL":
        y0 = y0 + max(1,h/2.0)
        x0 = x0 - max(1,w/2.0)
        h = h/2.0
        w = w/2.0
    elif bomb_dir == "UR":
        y0 = y0 - max(1,h/2.0)
        x0 = x0 + max(1,w/2.0)
        h = h/2.0
        w = w/2.0
    else:    
        y0 = y0 - max(1,h/2.0)
        x0 = x0 - max(1,w/2.0)
        h = h/2.0
        w = w/2.0

    print "{} {}".format(int(x0),int(y0))
