import sys
import math

while True:
    maxH = -1
    for i in xrange(8):
        mountain_h = int(raw_input())  # represents the height of one mountain.
        if mountain_h > maxH:
            maxH = mountain_h
            indexM = i

    print indexM
