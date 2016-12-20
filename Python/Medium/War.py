import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # the number of cards for player 1
deckp_1 = [] 
deckp_2 = []
table1 = []
table2 = []
tie = False
value = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,
    '8':7,'9':8,'1':9,'J':10,'Q':11,'K':12,'A':13
}
turns = 0
for i in xrange(n):
    cardp_1 = raw_input()  # the n cards of player 1
    deckp_1.append(cardp_1)
m = int(raw_input())  # the number of cards for player 2
for i in xrange(m):
    cardp_2 = raw_input()  # the m cards of player 2
    deckp_2.append(cardp_2)
# Write an action using print
while (deckp_1 and deckp_2 and not tie):
    table1.append(deckp_1.pop(0))
    table2.append(deckp_2.pop(0))
    if value[table1[-1][0]] == value[table2[-1][0]]:
        if len(deckp_1) > 3 and len(deckp_2) > 3:      
            for i in xrange(0,3):
                table1.append(deckp_1.pop(0))
                table2.append(deckp_2.pop(0))
        else:
            tie = True
        continue
    if value[table1[-1][0]] > value[table2[-1][0]]:
        for card in table1:
            deckp_1.append(card)
        for card in table2:
            deckp_1.append(card)
        table1 = []
        table2 = []
    else:
        for card in table1:
            deckp_2.append(card)
        for card in table2:
            deckp_2.append(card)
        table1 = []
        table2 = []
    turns += 1

if tie:
    print "PAT"
elif deckp_1:
    print "1 {}".format(turns)
else:
    print "2 {}".format(turns)
