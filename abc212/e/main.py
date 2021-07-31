N, M, K = map(int, input().split())
MOD = 998244353
road = [[True] * N for i in range(N)]

for i in range(M):
    u, v = map(int,input().split())
    u -= 1
    v -= 1
    road[u][v] = False
    road[v][u] = False
for i in range(N):
    road[i][i] = False

# cnt[x日目][今訪れている都市]
# cnt = [][] 
cnt = [[0] * N for i in range(K)]

cnt[0][0] = 1

for k in range(1, K):
    for n1 in range(N):
        for n2 in range(N):
            if road[n1][n2]:
                cnt[k][n1] += cnt[k-1][n2]
                cnt[k][n1] %= MOD
            # else:
            #     cnt[k][n1] = cnt[k-1][n1]

print(cnt[K-1][0])
