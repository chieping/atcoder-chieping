import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
color = [-1]*N
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append((b,w))
    edge[b].append((a,w))

def dfs(now, last=-1):
    for v, w in edge[now]:
        if v == last: continue
        if color[v] == -1:
            color[v] = abs(color[now] - (w%2))
            dfs(v, now)

color[0] = 0
dfs(0)
print(*color, sep='\n')
