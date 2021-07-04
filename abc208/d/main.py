INF = 10**18

N, M = map(int, input().split())

dist = [[INF] * N for i in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c

ans = 0

for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

    for i in range(N):
        for j in range(N):
            if dist[i][j] != INF:
                ans += dist[i][j]

print(ans)
