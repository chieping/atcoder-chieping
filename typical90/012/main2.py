# UnionFind 直書き
from sys import stdin
import sys
sys.setrecursionlimit(10**7)
H, W = map(int, stdin.readline().split())
Q = int(stdin.readline())
B = [[0] * (W+2) for _ in range(H+2)]
p = [-1] * ((H+1)*(W+1))

def root(x):
    if p[x] < 0:
        return x
    else:
        p[x] = root(p[x])
        return p[x]

def union(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    p[x] += p[y]
    p[y] = x

for _ in range(Q):
    q = list(map(int, stdin.readline().split()))
    if q[0] == 1:
        r, c = q[1:]
        B[r][c] = 1
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if B[r+dx][c+dy]:
                union(r*W+c, (r+dx)*W+(c+dy))
    elif q[0] == 2:
        ra, ca, rb, cb = q[1:]
        if B[ra][ca] and B[rb][cb] and root(ra*W+ca) == root(rb*W+cb):
            print('Yes')
        else:
            print('No')
