from itertools import imap

n = int(raw_input())
c = int(raw_input())
b = []
ans = []
for i in xrange(n):
    b.append(int(raw_input()))
   
b.sort()
if sum(b) < c:
    print 'IMPOSSIBLE'
else:
    for i in b:
        mean = c/n
        contrib = min(i, mean)
        ans.append(contrib)
        c += -contrib
        n += -1
    ans[-1] += c
    print '\n'.join(imap(str, ans))
