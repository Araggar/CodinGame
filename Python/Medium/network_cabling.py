import sys

max_x = -sys.maxint
min_x = sys.maxint
coord_y = []
sum_y = 0

n = int(raw_input())
for i in xrange(n):
    x, y = [int(j) for j in raw_input().split()]
    coord_y.append(y)
    min_x = min(min_x, x)
    max_x = max(max_x, x)

len_x = abs(max_x - min_x)
coord_y.sort()
median_y = coord_y[len(coord_y)/2]

for y in coord_y:
    sum_y += abs(y - median_y)

print len_x + sum_y
