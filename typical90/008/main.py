N = int(input())
S = ["X"] + list(input())
atcoder = "Xatcoder"
MOD = 10**9+7
dp = [[1] + [0] * 7 for i in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    for j in range(1, 8):
        if S[i] == atcoder[j]:
            dp[i][j] += (dp[i-1][j-1] + dp[i-1][j]) % MOD
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][7])
