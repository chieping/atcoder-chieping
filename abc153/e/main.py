import sys
readline = sys.stdin.readline
HP, N = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
INF = 10**18
dp = [INF] * (20010)
dp[0] = 0
for i in range(20005):
    next_dp = dp.copy()
    for a, b in AB:
        if i-a >= 0 and dp[i-a] != INF:
            next_dp[i] = min(next_dp[i], dp[i-a] + b)
    dp = next_dp
print(min(dp[HP:]))