import heapq

N, M = map(int, input().split())

G = [[] for i in range(N)]

for i in range(M):
    u, v, c = map(int, input().split())
    G[u].append([v, c])

dist = [-1 for i in range(N)]
dist[0] = 0

Q = []
heapq.heappush(Q, (0, 0))

done = [False] * N

while len(Q) > 0:
    d, i = heapq.heappop(Q)

    if done[i]:
        continue

    done[i] = True

    for (j, c) in G[i]:

        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heapq.heappush(Q, (dist[j], j))

print(dist[N-1])
