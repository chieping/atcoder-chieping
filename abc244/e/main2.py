N, M, K, S, T, X = map(int, input().split())
S -= 1
T -= 1
X -= 1
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append(b)
    edge[b].append(a)
MOD = 998244353

dp = []
for _ in range(N):
    dp.append([0, 0])
dp[S][0] = 1

for _ in range(K):
    prev = dp
    dp = []
    for _ in range(N):
        dp.append([0, 0])

    for u in range(N):
        for v in edge[u]:
            if v == X:
                dp[v][0] += prev[u][1]
                dp[v][1] += prev[u][0]
            else:
                dp[v][0] += prev[u][0]
                dp[v][1] += prev[u][1]

    for u in range(N):
        dp[u][0] %= MOD
        dp[u][1] %= MOD

print(dp[T][0])    
