# 解説AC
# 区間DP
from itertools import accumulate
N = int(input())
A = list(map(int, input().split()))
cum = [0] + list(accumulate(A))
INF = 10**18
flag = [[False] * (N+1) for _ in range(N+1)]
dp = [[0] * (N+1) for _ in range(N+1)]
def f(l, r):
    if flag[l][r]:
        return dp[l][r]
    flag[l][r] = True
    if l == r:
        return 0
    fans = INF
    for m in range(l, r):
        fans = min(fans, f(l, m) + f(m+1, r))
        dp[l][r] = fans + (cum[r] - cum[l-1])
    return dp[l][r]
print(f(1, N))