import sys
import math

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]

# game loop
while True:
    remaining_turns = int(raw_input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if light_x > initial_tx:
        if light_y > initial_ty:
            print "SE"
            initial_ty += 1
            initial_tx += 1
        elif light_y < initial_ty:
            print "NE"
            initial_ty += 1
            initial_tx += -1
        else:
            print "E"
            initial_tx += 1
    elif light_x < initial_tx:
        if light_y > initial_ty:
            print "SW"
            initial_ty += 1
            initial_tx += -1
        elif light_y < initial_ty:
            print "NW"
            initial_ty += -1
            initial_tx += -1
        else:
            print "W"
            initial_tx += -1
    else:
        if light_y > initial_ty:
            print "S"
            initial_ty += 1
        else:
            print "N"
            initial_ty += -1