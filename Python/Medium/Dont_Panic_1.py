import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in raw_input().split()]
elevators = {}
for i in xrange(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in raw_input().split()]
    elevators[elevator_floor] = elevator_pos

# game loop

while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = raw_input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    action = "WAIT"
    if clone_floor == exit_floor:
        if exit_pos - clone_pos < 0 and direction == "RIGHT":
            action = "BLOCK"
        elif exit_pos - clone_pos > 0 and direction == "LEFT":
            action = "BLOCK"
    
    if clone_floor in elevators:
        if elevators[clone_floor] - clone_pos < 0 and direction == "RIGHT":
            action = "BLOCK"
        elif elevators[clone_floor] - clone_pos > 0 and direction == "LEFT":
            action = "BLOCK"
    # action: WAIT or BLOCK
    print action
