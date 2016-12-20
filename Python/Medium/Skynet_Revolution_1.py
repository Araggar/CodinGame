import sys
import math

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in raw_input().split()]
lines = []
gates = []
used = []
for i in xrange(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in raw_input().split()]
    lines.append(str(n1)+" "+str(n2))
for i in xrange(e):
    ei = int(raw_input())  # the index of a gateway node
    gates.append(str(ei))
# game loop
while True:
    brk = False
    si = int(raw_input())  # The index of the node on which the Skynet agent is positioned this turn
    for gate in gates:
        for linkIndex in xrange(len(lines)):
            if gate in lines[linkIndex].split(" ") and str(si) in lines[linkIndex].split(" "):
                print >> sys.stderr, lines[linkIndex].split(" ")
                print lines.pop(linkIndex)
                brk = True
                break
        if brk:
            break
    else:
        brk = False
        for gate in gates:
            for linkIndex in xrange(len(lines)):
                if gate in lines[linkIndex].split(" "):
                    print >> sys.stderr, lines[linkIndex]
                    print lines.pop(linkIndex)
                    brk = True
                    break
            if brk:
                break