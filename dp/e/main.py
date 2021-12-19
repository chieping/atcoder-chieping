N, W = map(int, input().split())
MV = 10**3*N
INF = 10**18
dp = [[INF] * (MV+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in range(MV+1):
        if j-v >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v]+w)
        else:
            dp[i][j] = dp[i-1][j]
j = MV
while dp[N][j] > W:
    j -= 1
print(j)
