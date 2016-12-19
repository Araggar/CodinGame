import sys
import math

l = int(raw_input())
h = int(raw_input())
t = raw_input()
lines = []
dic = {
    'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6, 'h':7,
    'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14, 'p':15,
    'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22, 'x':23,
    'y':24,'z':25, '?':26
    }
for i in xrange(h):
    row = raw_input()
    lines.append(row)
t = str.lower(t)
for line in lines:
    resp = []
    for letters in t:
        if letters in dic:
            resp.append(line[0 + l*dic[letters] : l + l*dic[letters]])
        else:          
            resp.append(line[l*26 : l + l*26])
    print "".join(resp)

