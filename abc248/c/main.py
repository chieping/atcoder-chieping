import sys
input = sys.stdin.readline
MOD = 998244353
N, M, K = map(int, input().split())

dp = [[0] * 2510 for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(2501):
        if dp[i][j] > 0:
            for k in range(1, M+1):
                dp[i+1][j+k] += dp[i][j]
                dp[i+1][j+k] %= MOD

print(sum(dp[N][:K+1])%MOD)