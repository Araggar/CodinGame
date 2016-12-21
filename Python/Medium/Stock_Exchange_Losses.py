import sys
import math

bigV = 0
dif = 0
stock = []
n = int(raw_input())
for i in raw_input().split():
    v = int(i)
    bigV = max(bigV,v)
    dif = min(dif,v - bigV)

print dif

