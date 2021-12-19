from collections import defaultdict
N, W = map(int, input().split())
dp = [defaultdict(int) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    w, nv = map(int, input().split())
    for k, cv in dp[i-1].items():
        dp[i][k] = max(dp[i][k], cv)
        if k+w <= W:
            dp[i][k+w] = max(dp[i][k+w], cv+nv)
print(max(dp[N].values()))
