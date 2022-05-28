MOD = 998244353
N, M, K = map(int, input().split())

dp = [[0] * (M+1) for _ in range(N)]

for i in range(1, M+1):
    dp[0][i] = 1

for i in range(1, N):
    c = [0] * (M+1)
    for j in range(M+1):
        c[j] = dp[i-1][j]
        if j > 0:
            c[j] += c[j-1]
    for j in range(1, M+1):
        if 0 <= j - K:
            dp[i][j] += c[j-K]
        if j + K <= M:
            if K != 0:
                dp[i][j] += c[-1] - c[j+K-1]
            else:
                dp[i][j] += c[-1] - c[j]
        dp[i][j] %= MOD
ans = 0
for r in dp[-1]:
    ans += r
    ans %= MOD
print(ans)
# for i in range(N+1):
#     print(dp[i])
