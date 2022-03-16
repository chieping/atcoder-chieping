import sys
readline = sys.stdin.readline
S = list(input())
T = list(-1 if c == '?' else int(c) for c in S)
MOD = 10**9+7
dp = [0] * 13
dp[0] = 1

for n in T: # 疑問：なぜ上の桁から処理でいいのか？
    prev = dp
    dp = [0] * 13
    for i in range(10):
        if n != -1 and i != n:
            continue
        for m in range(13):
            dp[(m * 10 + i) % 13] += prev[m]
    dp = [i%MOD for i in dp]
print(dp[5])