N = int(input())

dp = [[0, 0, 0] for i in range(N)]

# 初回
dp[0] = list(map(int, input().split()))

for i in range(1, N):
    a, b, c = map(int, input().split())
    dp[i][0] = max(dp[i-1][1] + a, dp[i-1][2] + a)
    dp[i][1] = max(dp[i-1][0] + b, dp[i-1][2] + b)
    dp[i][2] = max(dp[i-1][0] + c, dp[i-1][1] + c)

print(max(dp[N-1]))
