from pprint import pprint
import sys
input = sys.stdin.readline
N, M, K, S, T, X = map(int, input().split())
X -= 1
S -= 1
T -= 1
MOD = 998244353
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

# Xが偶数、奇数
dp = []
for _ in range(N):
    dp.append([0, 0])
dp[S] = [1, 0]

for _ in range(K):
    nxt_dp = []
    for _ in range(N):
        nxt_dp.append([0, 0])
    for i in range(N):
        for v in edge[i]:
            if v == X:
                nxt_dp[v][0] += dp[i][1]
                nxt_dp[v][0] %= MOD
                nxt_dp[v][1] += dp[i][0]
                nxt_dp[v][1] %= MOD 
            else:
                nxt_dp[v][0] += dp[i][0]
                nxt_dp[v][0] %= MOD
                nxt_dp[v][1] += dp[i][1]
                nxt_dp[v][1] %= MOD
    dp = nxt_dp

print(dp[T][0])


