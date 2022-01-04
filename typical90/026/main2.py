# 二部グラフの彩色
from sys import stdin
import sys
sys.setrecursionlimit(10**6)
N = int(stdin.readline())
edges = [[] for _ in range(N+1)]
colors = [-1] * (N+1)
for _ in range(N-1):
    a, b = map(int, stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

def dfs(v, color):
    colors[v] = color
    for next in edges[v]:
        if colors[next] == -1:
            dfs(next, abs(color-1))

dfs(1, 0)

ans = [idx for idx, v in enumerate(colors) if v == 0]
if len(ans) < N//2:
    ans = [idx for idx, v in enumerate(colors) if v == 1]
print(*ans[0:N//2])
