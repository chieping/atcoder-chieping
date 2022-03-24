import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [True] * (N+1)
for _ in range(M):
    A[int(input())] = False
MOD = 10**9+7
dp = [0] * (N+1)
dp[0] = 1
for i in range(1, N+1):
    if A[i]:
        dp[i] += dp[i-1]
        if i-2 >= 0:
            dp[i] += dp[i-2]
        dp[i] %= MOD
print(dp[N])

