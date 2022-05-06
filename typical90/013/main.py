from heapq import heappop, heappush
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append((b, c))
    edge[b].append((a, c))

def dijkstra(start):
    dist = [-1] * N
    dist[start] = 0
    Q = []
    heappush(Q, (0, start))
    done = [False] * N

    while len(Q):
        _d, i = heappop(Q)
        if done[i]:
            continue
        done[i] = True

        for j, c in edge[i]:
            if dist[j] == -1 or dist[j] > dist[i] + c:
                dist[j] = dist[i] + c
                heappush(Q, (dist[j], j))
    return dist

# 街1からの最短路と、
# 街Nからの最短路を求め、
# その2つの結果を使って答える
dist1 = dijkstra(0)
distN = dijkstra(N-1)

for k in range(N):
    print(dist1[k] + distN[k])
