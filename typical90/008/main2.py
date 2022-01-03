# DP
N = int(input())
S = list(input())
atcoder = dict(zip('atcoder', range(1, 8)))
MOD = 10**9+7
S = [atcoder[s] for s in S if s in atcoder]
N = len(S)

dp = [0] * 8
dp[0] = 1

for s in S:
    dp[s] += dp[s-1]
    dp[s] %= MOD

print(dp[7])
