from collections import deque
import sys
readline = sys.stdin.readline
N, Q = map(int, readline().split())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
C = [0] * N
for _ in range(Q):
    p, x = map(int, readline().split())
    p -= 1
    C[p] += x
ans = [0] * N

# BFSで根から計算
q = deque()
visited = [False] * N
q.append(0)
while len(q) > 0:
    v = q.popleft()
    visited[v] = True
    ans[v] += C[v]
    for t in edges[v]:
        if visited[t]:
            continue
        ans[t] += ans[v]
        q.append(t)

print(*ans)
