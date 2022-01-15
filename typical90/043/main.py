# 01-BFS
from collections import deque
import sys
readline = sys.stdin.readline
H, W = map(int, readline().split())
rs, cs = map(int, readline().split())
rs, cs = rs-1, cs-1
rt, ct = map(int, readline().split())
rt, ct = rt-1, ct-1
S = [readline()[:-1] for _ in range(H)]
INF = 10**18
dx = [0, 1]
dy = [1, 0]
start = 2*H*W
goal = start + 1

def ind(i, j, d):
    return (i * W + j) * 2 + d

edge0 = [[] for _ in range(2 * H * W + 2)]
edge1 = [[] for _ in range(2 * H * W + 2)]
dist = [INF] * (2*H*W+2)

for d in range(2):
    edge0[start].append(ind(rs, cs, d))
    edge0[ind(rt, ct, d)].append(goal)

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        for d in range(2):
            d2 = (d+1) % 2
            edge1[ind(i,j,d)].append(ind(i,j,d2))
            ni = i + dx[d]
            nj = j + dy[d]
            if not(ni < 0 or ni >= H or nj < 0 or nj >= W) and S[ni][nj] == '.':
                edge0[ind(i,j,d)].append(ind(ni,nj,d))
            ni = i - dx[d]
            nj = j - dy[d]
            if not(ni < 0 or ni >= H or nj < 0 or nj >= W) and S[ni][nj] == '.':
                edge0[ind(i,j,d)].append(ind(ni,nj,d))

dq = deque()
dq.append(start)
dist[start] = 0

while len(dq) > 0:
    now = dq.popleft()
    if now == goal:
        print(dist[now])
        exit()
    for to in edge0[now]:
        if dist[to] > dist[now]:
            dist[to] = dist[now]
            dq.appendleft(to)
    for to in edge1[now]:
        if dist[to] > dist[now] + 1:
            dist[to] = dist[now] + 1
            dq.append(to)
