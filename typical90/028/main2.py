# 二次元いもす法
from collections import Counter
from itertools import chain
from sys import stdin
N = int(stdin.readline())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]
B = [[0] * 1010 for _ in range(1010)]

for lx, ly, rx, ry in A:
    B[lx][ly] += 1
    B[lx][ry] -= 1
    B[rx][ly] -= 1
    B[rx][ry] += 1

for i in range(1001):
    for j in range(1001):
        B[i+1][j] += B[i][j]
for i in range(1001):
    for j in range(1001):
        B[i][j+1] += B[i][j]

c = Counter(chain.from_iterable(B))

for i in range(1, N+1):
    print(c[i])
