N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [10**18] * N
dp[0] = 0

for i in range(1, N):
    m = 10**18
    for j in range(1, K+1):
        if i < j:
            break
        m = min(m, dp[i-j]+abs(h[i]-h[i-j]))
    dp[i] = m

print(dp[N-1])
