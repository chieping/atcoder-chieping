# TLE
from collections import deque
N, M = map(int, input().split())
H = list(map(int, input().split()))
G = [[] for _ in range(N)]

def fun(u, v):
    if H[u] >= H[v]:
        return H[u] - H[v]
    else:
        return 2 * (H[u] - H[v])

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    G[u].append((fun(u, v), v))
    G[v].append((fun(v, u), u))

INF = 10**18
Q = deque()
Q.append((0, 0))
visited = [-INF] * N
visited[0] = 0
while len(Q):
    now_loc, now_fun = Q.popleft()
    if visited[now_loc] > now_fun:
        continue

    for fun, v in G[now_loc]:
        next_fun = now_fun + fun
        if visited[v] < next_fun:
            visited[v] = next_fun
            Q.append((v, next_fun))

print(max(visited))
