import sys
import math

n = int(raw_input())
horses = []
for i in xrange(n):
    pi = int(raw_input())
    horses.append(pi)
horses.sort()
dif = sys.maxint
for x in xrange(len(horses)-1):
    if abs(horses[x]-horses[x+1]) < dif:
        dif = abs(horses[x]-horses[x+1])
print dif