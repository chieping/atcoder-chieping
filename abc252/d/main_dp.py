from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = list(Counter(A).values())
M = len(B)
dp = [0] * 4
dp[0] = 1
for cnt in B:
    prev = dp.copy()
    dp[1] += prev[0] * cnt
    dp[2] += prev[1] * cnt
    dp[3] += prev[2] * cnt
print(dp[3])
