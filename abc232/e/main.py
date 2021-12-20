H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
MOD = 998244353
dp = [[0, 0] for i in range(2)]
dp[1 if x1==x2 else 0][1 if y1==y2 else 0] = 1
for _ in range(K):
    prev = dp
    dp = [[0, 0] for _ in range(2)]
    for j in range(2):
        dp[0][j] += prev[0][j]*(H-2)
        dp[0][j] %= MOD
        dp[1][j] += prev[0][j]
        dp[1][j] %= MOD
        dp[0][j] += prev[1][j]*(H-1)
        dp[0][j] %= MOD
    for i in range(2):
        dp[i][0] += prev[i][0]*(W-2)
        dp[i][0] %= MOD
        dp[i][1] += prev[i][0]
        dp[i][1] %= MOD
        dp[i][0] += prev[i][1]*(W-1)
        dp[i][0] %= MOD
print(dp[1][1])
