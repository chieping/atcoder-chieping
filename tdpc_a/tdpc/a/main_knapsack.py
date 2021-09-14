N = int(input())
P = list(map(int, input().split()))

dp = [[False] * (N * 100) for i in range(N + 1)]

dp[0][0] = True

for i in range(1, N + 1):
    for j in range(N * 100):
        dp[i][j] = dp[i-1][j]
        if j - P[i-1] >= 0:
            dp[i][j] |= dp[i-1][j-(P[i-1])]    

print(sum(dp[N]))
