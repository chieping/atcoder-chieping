from itertools import accumulate
N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9+7
dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1
for i, a in enumerate(A, 1):
    cum = [0] + list(accumulate(dp[i-1]))
    for j in range(K+1):
        dp[i][j] = (cum[j+1] - cum[max(0, j-a)] + MOD)%MOD
print(dp[N][K])