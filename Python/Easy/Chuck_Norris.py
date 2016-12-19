import sys
import math

message = raw_input()
this = map(bin,bytearray(message))
for i in range(0,len(this)):
    while len(this[i])<9:
        this[i] = this[i][0:2]+"0"+this[i][2:]
print >> sys.stderr, this
that = []
lastL = this[0][2]
count = 0
for thing in this:
    for letters in thing[2::]:
        if lastL == letters:
            count += 1            
        else:
            if letters == "1":
                that.append("00 "+"0"*count)
                count = 1
                lastL = "1"
            else:
                that.append("0 "+"0"*count)
                count = 1
                lastL = "0"

if lastL == "1":
    that.append("0 "+"0"*count)
else:
    that.append("00 "+"0"*count)
    
print " ".join(that)
