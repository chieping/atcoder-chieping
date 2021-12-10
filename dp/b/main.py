N, K = map(int, input().split())
h = [0] + list(map(int, input().split()))
dp = [10**18] * (N+1)
dp[0] = 0
dp[1] = 0
for i in range(2, N+1):
    for j in range(1, K+1):
        if i-j > 0:
            dp[i] = min(dp[i], dp[i-j] + abs(h[i]-h[i-j]))
print(dp[N])
