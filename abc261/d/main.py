from collections import defaultdict
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
X = list(map(int, input().split()))
C = defaultdict(int)
for i in range(M):
    c, y = map(int, input().split())
    C[c] = y

dp = []
for _ in range(N+1):
    dp.append([0] * (N+1))

Max = 0
for i in range(1, N+1):
    for j in range(1, i+1):
        # 表の場合
        dp[i][j] = dp[i-1][j-1] + X[i-1] + C[j]

    # 裏の場合
    dp[i][0] = max(dp[i-1])

print(max(dp[N]))