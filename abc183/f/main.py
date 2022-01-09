from collections import defaultdict
from sys import stdin
N, Q = map(int, stdin.readline().split())
C = list(map(int, stdin.readline().split()))
parents = [-1] * (N+1)

def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    if parents[x] > parents[y]:
        x, y = y, x
    parents[x] += parents[y]
    parents[y] = x

def root(x):
    if parents[x] < 0:
        return x
    parents[x] = root(parents[x])
    return parents[x]
    
member = [defaultdict(int) for _ in range(N)]

for i, c in enumerate(C):
    member[i][c-1] = 1

for _ in range(Q):
    com, x, y = map(int, stdin.readline().split())
    x -= 1
    y -= 1
    if com == 1:
        x = root(x)
        y = root(y)
        if x != y:
            if parents[x] > parents[y]:
                x, y = y, x
            unite(x, y)
            for k, v in member[y].items():
                member[x][k] += v

    elif com == 2:
        print(member[root(x)][y])
