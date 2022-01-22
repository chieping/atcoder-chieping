# LCS (Longest Common Subsequence) (蟻本P56)
# LIS (Longest Increasing Subsequence) (蟻本P63)

from bisect import bisect_left
import sys
readline = sys.stdin.readline

N = int(readline())
P = list(map(int, readline().split()))
Q = list(map(int, readline().split()))

Qpos = [-1] * (N+1)
for i in range(N):
    Qpos[Q[i]] = i

INF = 10**10
dp = [-1] + [INF] * (N+1)

for a in P:
    targets = [Qpos[j] for j in range(a, N+1, a)]
    targets.sort(reverse=True)
    for j in targets:
        k = bisect_left(dp, j)
        dp[k] = j
ans = 0
while dp[ans+1] != INF:
    ans += 1
print(ans)

