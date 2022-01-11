# 部分和問題 DP
import sys
readline = sys.stdin.readline
N = int(readline())
T = list(map(int, readline().split()))
S = sum(T)

dp = [False] * (S+1)
dp[0] = True

for i in range(N):
    prev = dp.copy()
    for j in range(S+1):
        if j-T[i] >= 0:
            dp[j] |= prev[j-T[i]]

for i in range((S+1)//2, S+1):
    if dp[i]:
        print(i)
        exit()
