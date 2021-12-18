N = int(input())
S = [input() for i in range(N)]
dp = [[0] * 2 for i in range(N+1)]
dp[0][0] = 1
dp[0][1] = 1
for i in range(1, N+1):
    s = S[i-1]
    # x=0の場合
    if s == 'AND':
        dp[i][0] += dp[i-1][0] + dp[i-1][1]
    elif s == 'OR':
        dp[i][0] += dp[i-1][0]
        dp[i][1] += dp[i-1][1]
    # x=1の場合
    if s == 'AND':
        dp[i][0] += dp[i-1][0]
        dp[i][1] += dp[i-1][1]
    elif s == 'OR':
        dp[i][1] += dp[i-1][0] + dp[i-1][1]
print(dp[N][1])
