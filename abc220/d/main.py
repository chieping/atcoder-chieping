N = int(input())
A = list(map(int, input().split()))
P = 998244353
# dp[i][j] = n
# i: i回目の操作
# j: 左端の数
# n: 経路数
dp = [[0] * 10 for i in range(N)]

# 初期値
dp[0][A[0]] = 1

for i in range(1, N):
    for j in range(10):
        fa = (j+A[i]) % 10
        dp[i][fa] += dp[i-1][j]
        dp[i][fa] %= P

        fb = (j*A[i]) % 10
        dp[i][fb] += dp[i-1][j]
        dp[i][fb] %= P

for i in range(10):
    print(dp[N-1][i])
