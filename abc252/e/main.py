# WA
from heapq import heappop, heappush
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(1, M+1):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append((c, b, i))
    edge[b].append((c, a, i))

ans = set()

def dijkstra(v):
    Q = []
    dist = [-1] * N
    done = [False] * N
    dist[0] = 0
    done[0] = True
    for c, j, i in edge[0]:
        heappush(Q, (c, j, i))
    
    while len(Q):
        c, j, i = heappop(Q)

        if done[j]:
            continue
        done[j] = True

        ans.add(i)

        for cc, jj, ii in edge[j]:
            if dist[jj] == -1 or dist[jj] > dist[j] + cc:
                dist[jj] = dist[j] + cc
                heappush(Q, (dist[jj], jj, ii))

for v in range(1, N):
    dijkstra(v)

print(*ans)
