# TLE
from pprint import pprint
from sys import stdin
H, W = map(int, stdin.readline().split())
S = [list(stdin.readline()[:-1]) for _ in range(H)]
MOD = 10**9+7
dp = [[0] * (W+2) for _ in range(H+2)]
dp[1][1] = 1
for i in range(1, H+1):
    for j in range(1, W+1):
        if S[i-1][j-1] == '#':
            continue
        # 左から来た場合
        k = i - 1
        while k > 0 and S[k-1][j-1] != '#':
            dp[i][j] += dp[k][j]
            dp[i][j] %= MOD
            k -= 1
        # 上から来た場合
        k = j - 1
        while k > 0 and S[i-1][k-1] != '#':
            dp[i][j] += dp[i][k]
            dp[i][j] %= MOD
            k -= 1
        # 斜め上から来た場合
        k = i - 1
        l = j - 1
        while k > 0 and l > 0 and S[k-1][l-1] != '#':
            dp[i][j] += dp[k][l]
            dp[i][j] %= MOD
            k -= 1
            l -= 1
print(dp[H][W])
