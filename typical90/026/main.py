import sys
sys.setrecursionlimit(10**6)
N = int(input())
G = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# 彩色する
colors = [-1] * (N+1)

def dfs(pos, cur):
    colors[pos] = cur
    for v in G[pos]:
        if colors[v] == -1:
            dfs(v, 1-cur)

dfs(1, 1)

red = []
green = []
for i in range(N+1):
    if colors[i] == 1:
        red.append(i)
    elif colors[i] == 0:
        green.append(i)
if len(red) >= len(green):
    ans = red
else:
    ans = green
print(*ans[0:(N//2)])
