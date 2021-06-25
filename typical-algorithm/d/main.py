from collections import deque

N, M = map(int, input().split())

G = [[] for i in range(N)]

for i in range(M):
    u, v, c = map(int, input().split())
    G[u].append([v, c])

cost = [10**8 for i in range(N)]
cost[0] = 0

visited = [False] * N
visited[0] = True

Q = deque()

Q.append(0)

while len(Q) > 0:
    i = Q.popleft()

    for j, c in G[i]:
        cost[j] = min(cost[j], cost[i] + c)
        if not visited[j]:
            Q.append(j)
        visited[j] = True

print(cost[N-1])
