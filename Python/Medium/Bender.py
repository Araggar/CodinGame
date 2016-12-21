import sys
import math

l, c = [int(i) for i in raw_input().split()]
mapc = []
past_states = []
telep = []
direction = "SOUTH"
ans = []
beer = False
invert = False
moddirection = ''
directions = {"SOUTH":(0,1),"EAST":(1,0),"NORTH":(0,-1),"WEST":(-1,0)}
ret = ["SOUTH","EAST","NORTH","WEST"]
for i in xrange(l):
    row = raw_input()
    mapc.append(row)
    if '@' in row:
        coords = [row.index('@'),i]
    if 'T' in row:
        telep.append([row.index('T'),i])

end_state = '{}{}{}{}'.format(coords,direction,beer,invert)

while (end_state not in past_states):
    #if end_state in past_states:
    #    ans = ['LOOP']
    #    break
    
    ind = 0
    past_states.append('{}{}{}{}'.format(coords,direction,beer,invert))
    
    if mapc[coords[1]][coords[0]] == 'T':
        if coords == telep[0]:
            coords[1] = telep[1][1]
            coords[0] = telep[1][0]
        else:
            coords[1] = telep[0][1]
            coords[0] = telep[0][0]
    
    if mapc[coords[1]][coords[0]] == 'B':
        beer = not beer
        
    while mapc[coords[1]+directions[direction][1]][coords[0]+directions[direction][0]] in '#X':
        if mapc[coords[1]+directions[direction][1]][coords[0]+directions[direction][0]] in "#":
            direction = ret[ind]
            ind += 1
        if mapc[coords[1]+directions[direction][1]][coords[0]+directions[direction][0]] in "X":
            if beer:
                mapc[coords[1]+directions[direction][1]] = mapc[coords[1]+directions[direction][1]][0:coords[0]+directions[direction][0]]+" "+mapc[coords[1]+directions[direction][1]][coords[0]+directions[direction][0]+1:]
                past_states = []
            else:
                direction = ret[ind]
                ind += 1
    
    if moddirection:
        direction = moddirection
        moddirection = ''
    elif mapc[coords[1]+directions[direction][1]][coords[0]+directions[direction][0]] == 'S':
        moddirection = 'SOUTH'
    elif mapc[coords[1]+directions[direction][1]][coords[0]+directions[direction][0]] == 'E':
        moddirection = 'EAST'
    elif mapc[coords[1]+directions[direction][1]][coords[0]+directions[direction][0]] == 'N':
        moddirection = 'NORTH'
    elif mapc[coords[1]+directions[direction][1]][coords[0]+directions[direction][0]] == 'W':
        moddirection = 'WEST' 
        
    elif mapc[coords[1]+directions[direction][1]][coords[0]+directions[direction][0]] == 'I':
        ret = ret[::-1]
    elif mapc[coords[1]+directions[direction][1]][coords[0]+directions[direction][0]] == '$':
        ans.append(str(direction))
        break
        
    coords[0] = coords[0] + directions[direction][0]
    coords[1] = coords[1] + directions[direction][1]
    ans.append(str(direction))
    end_state = '{}{}{}{}'.format(coords,direction,beer,invert)
else:
    ans = ['LOOP']
for single in ans:
    print single
