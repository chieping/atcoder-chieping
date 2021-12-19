N = int(input())
P = [0] + list(map(float, input().split()))
dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 1.0
for i in range(1, N+1):
    for j in range(N):
        dp[i][j] += dp[i-1][j] * (1-P[i])
        dp[i][j+1] += dp[i-1][j] * P[i]
print(sum(dp[N][(N+1)//2:]))
