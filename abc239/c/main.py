import sys
readline = sys.stdin.readline
x1, y1, x2, y2 = map(int, readline().split())
s1 = set()
s2 = set()
d = [(1,2),(2,1),(2,-1),(1,-2),(-1,2),(-2,1),(-2,-1),(-1,-2)]

for dx,dy in d:
    s1.add((x1+dx,y1+dy))
    s2.add((x2+dx,y2+dy))

if len(s1.intersection(s2)) > 0:
    print('Yes')
else:
    print('No')