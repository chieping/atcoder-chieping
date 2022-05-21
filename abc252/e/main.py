# WA
from heapq import heappop, heappush
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(1, M+1):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append((c, b, i))
    edge[b].append((c, a, i))

marked = [False] * N
marked_count = 0

marked[0] = True
marked_count = 1

Q = []
ans = []
for c, j, i in edge[0]:
    heappush(Q, (c, j, i))

while marked_count < N:
    c, v, i = heappop(Q)

    if marked[v]:
        continue
    marked[v] = True
    marked_count += 1
    ans.append(i)

    for cc, vv, ii in edge[v]:
        if marked[vv]:
            continue
        heappush(Q, (cc, vv, ii))

print(*ans)