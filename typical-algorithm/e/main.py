INF = 10**20

N, M = map(int, input().split())

dist = [[INF for i in range(N)] for i in range(N)]

for _ in range(0, M):
    u, v, c = map(int, input().split())
    dist[u][v] = c

for i in range(0, N):
    dist[i][i] = 0

# ワーシャル・フロイド法
for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

ans = 0
for i in range(N):
    for j in range(N):
        ans += dist[i][j]

print(ans)
