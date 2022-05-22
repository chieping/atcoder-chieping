from heapq import heappop, heappush
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(1, M+1):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    # to, cost, edge_id
    edge[a].append((b, c, i))
    edge[b].append((a, c, i))

INF = 10**18
ans = [-1] * N
dist = [INF] * N
dist[0] = 0
Q = []
heappush(Q, (0, 0))
while len(Q):
    d, v = heappop(Q)
    if dist[v] != d:
        continue
    for u, cost, i in edge[v]:
        now_d = d + cost
        if dist[u] <= now_d:
            continue
        dist[u] = now_d
        ans[u] = i
        heappush(Q, (now_d, u))
print(*ans[1:])
