# Nが30以下の場合WA
from pprint import pprint
import sys
readline = sys.stdin.readline
N, lim = map(int, readline().split())
V = []
W = []
for _ in range(N):
    v, w = map(int, readline().split())
    V.append(v)
    W.append(w)

def solveByWeight():
    dp = [[-1] * (N*1000+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(N*1000+1):
            if j > lim:
                break
            if j-W[i] >= 0 and dp[i][j-W[i]] >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i][j-W[i]] + V[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(max(dp[N]))

def solveByValue():
    INF = 10**18
    dp = [[INF] * (N*1000+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(N*1000+1):
            if j-V[i] >= 0 and dp[i][j-V[i]] != INF:
                dp[i+1][j] = min(dp[i][j], dp[i][j-V[i]] + W[i])
            else:
                dp[i+1][j] = dp[i][j]
    ans = 0
    for i, w in list(enumerate(dp[N]))[::-1]:
        if w <= lim:
            ans = i
            break
    print(ans)

def solveByN():
    pprint(N)

if max(W) <= 1000:
    solveByWeight()
elif max(V) <= 1000:
    solveByValue()
else:
    solveByN()
