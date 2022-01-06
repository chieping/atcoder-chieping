from itertools import permutations
from sys import stdin
N, K = map(int, stdin.readline().split())
T = [list(map(int, stdin.readline().split())) for _ in range(N)]
# 全探索で間に合う

ans = 0
for p in permutations(range(1, N)):
    p = (0, *p, 0)
    cost = 0
    for i in range(len(p)-1):
        cost += T[p[i]][p[i+1]]
    if cost == K:
        ans += 1

print(ans)

