import sys
input = sys.stdin.readline
H, N = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
INF = 10**9
dp = [INF] * (2*10**4+1)
dp[0] = 0
for i in range(1, 2*10**4+1):
    prev = dp.copy()
    for a, b in zip(A, B):
        if i - a >= 0:
            dp[i] = min(dp[i], prev[i-a] + b)
print(min(dp[H:]))
