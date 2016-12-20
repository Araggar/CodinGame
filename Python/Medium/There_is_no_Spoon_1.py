import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(raw_input())  # the number of cells on the X axis
height = int(raw_input())  # the number of cells on the Y axis
lineList = []
nodes = []
for i in xrange(height):
    line = raw_input()# width characters, each either 0 or .
    lineList.append(line)

for y in range(height):
    for x in range(width):
        if lineList[y][x] == "0":
            nodes.append(str(x))
            nodes.append(str(y))
            
            for inc in range(1,(width-x)):
                if lineList[y][x+inc] == "0":
                    nodes.append(str(x+inc))
                    nodes.append(str(y))
                    break
            else:
                    nodes.append("-1 -1")            
            for inc in range(1,(height-y)):
                if lineList[y+inc][x] == "0":
                    nodes.append(str(x))
                    nodes.append(str(y+inc))
                    break
            else:
                    nodes.append("-1 -1")
            print " ".join(nodes)
        nodes = []
                
                
