import sys
import math

n = int(raw_input())  # the number of temperatures to analyse
temps = raw_input()# the n temperatures expressed as integers ranging from -273 to 5526
temps = temps.split(" ")
if n==0:
    print 0
else:
    intTemps = []
    for temp in temps:
        intTemps.append(int(temp))
    closestTemp = intTemps[0]
    for temp in intTemps:
        if math.fabs(temp) < math.fabs(closestTemp):
            closestTemp = temp
        elif math.fabs(temp) == math.fabs(closestTemp):
            if temp > closestTemp:
                closestTemp = temp
    print closestTemp
