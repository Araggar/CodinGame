map_lines = []
teleporters = []
past_states = []
ans = []
directions = {
              'SOUTH': (0,1),
              'EAST': (1,0),
              'NORTH': (0,-1),
              'WEST': (-1,0),
              }
priorities = ['SOUTH', 'EAST', 'NORTH', 'WEST']
beer = False
inverted = False
current_dir = 'SOUTH'

l, c = [int(i) for i in raw_input().split()]
for i in xrange(l):
    row = raw_input()
    map_lines.append(row)
    if '@' in row:
        start_xy = [row.index('@'), i]
    if 'T' in row:
        teleporters.append([row.index('T'), i])
    if '$' in row:
        final_xy = [row.index('$'), i]

#Game loop
while True: 
    #Loop condition
    if (str(start_xy), beer, inverted, current_dir) in past_states:
        ans = ['LOOP']
        break
    past_states.append((str(start_xy), beer, inverted, current_dir))
    #Ending condition
    if start_xy == final_xy:
        break
    #Instant changes
    elif map_lines[start_xy[1]][start_xy[0]] == 'S':
        current_dir = 'SOUTH'
    elif map_lines[start_xy[1]][start_xy[0]] == 'E':
        current_dir = 'EAST'
    elif map_lines[start_xy[1]][start_xy[0]] == 'N':
        current_dir = 'NORTH'
    elif map_lines[start_xy[1]][start_xy[0]] == 'W':
        current_dir = 'WEST'
    #Inverters
    elif map_lines[start_xy[1]][start_xy[0]] == 'I':
        priorities.reverse()
        inverted = not inverted
    #Breaker mode    
    elif map_lines[start_xy[1]][start_xy[0]] == 'B':
        beer = not beer
    #Teleporters
    elif map_lines[start_xy[1]][start_xy[0]] == 'T':
        if start_xy == teleporters[0]:
            start_xy = teleporters[1]
        else:
            start_xy = teleporters[0]
    #Obstacle #
    try:
        i = 0
        while map_lines[start_xy[1]+directions[current_dir][1]]\
                        [start_xy[0]+directions[current_dir][0]] == '#':
            current_dir = priorities[i]
            i += 1
    except IndexError:
        ans = ['LOOP']
        break
    #Obstacle X
    try:
        i = 0
        while map_lines[start_xy[1]+directions[current_dir][1]]\
                            [start_xy[0]+directions[current_dir][0]] == 'X':
            if beer:
                map_lines[start_xy[1]+directions[current_dir][1]] = \
                    map_lines[start_xy[1]+directions[current_dir][1]][:start_xy[0]+directions[current_dir][0]]\
                    +' '\
                    +map_lines[start_xy[1]+directions[current_dir][1]][start_xy[0]+directions[current_dir][0]+1:]
                past_states = []
            else:
                current_dir = priorities[i]
                i += 1
    except IndexError:
        ans = ['LOOP']
        break

    ans.append(current_dir)
    start_xy = [start_xy[0]+directions[current_dir][0], start_xy[1]+directions[current_dir][1]]

for direction in ans:
    print direction
