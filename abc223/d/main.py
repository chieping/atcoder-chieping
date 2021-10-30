
from heapq import heappop, heappush

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
indeg = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    indeg[b] += 1

q = []

for i in range(1, N+1):
    if indeg[i] == 0:
        heappush(q, i)

ans = []

while len(q) != 0:
    v = heappop(q)
    ans.append(v)
    for to in edges[v]:
        indeg[to] -= 1
        if indeg[to] == 0:
            heappush(q, to)

if len(ans) == N:
    print(*ans)
else:
    print(-1)
