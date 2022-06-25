import sys
input = sys.stdin.readline
N = int(input())
X = []
Y = []
P = []
for _ in range(N):
    x, y, p = map(int, input().split())
    X.append(x)
    Y.append(y)
    P.append(p)

INF = 10**18
dist = [[INF] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0

# for k in range(N):
#     for x in range(N):
#         for y in range(N):
#             dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

# print(dist)

ans = 10**18

for i in range(N):
    for j in range(N):
        if i == j: dist[i][j] = 0
        d = abs(X[i]-X[j]) + abs(Y[i]-Y[j])
        dist[i][j] = (d+P[i]-1)//P[i]

for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = max(dist[x][y], dist[x][k] + dist[k][y])
print(dist)
print(ans)