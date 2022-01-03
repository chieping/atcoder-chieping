# 木の直径
from collections import deque
from sys import stdin
N = int(stdin.readline())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, stdin.readline().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

def farthest_vert(start):
    q = deque()
    visited = [False] * N
    q.append((start, 0))
    while len(q) > 0:
        v = q.popleft()
        last = v
        visited[v[0]] = True
        for next in edges[v[0]]:
            if not visited[next]:
                q.append((next, v[1]+1))
    return last

v = farthest_vert(0)
dist = farthest_vert(v[0])[1]
print(dist+1)
