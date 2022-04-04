# 木DP
N = int(input())
C = input().split()
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append(b)
    edge[b].append(a)
MOD = 10**9+7
dp = [[0]*4 for _ in range(N)]

def dfs(pos, last=-1):
    val1 = 1; val2 = 1
    for to in edge[pos]:
        if to == last:
            continue
        dfs(to, pos)
        if C[pos] == 'a':
            val1 *= dp[to][0] + dp[to][2]
            val2 *= dp[to][0] + dp[to][1] + 2 * dp[to][2]
        if C[pos] == 'b':
            val1 *= dp[to][1] + dp[to][2]
            val2 *= dp[to][0] + dp[to][1] + 2 * dp[to][2]
        val1 %= MOD
        val2 %= MOD

    if C[pos] == 'a':
        dp[pos][0] = val1
        dp[pos][2] = (val2 - val1 + MOD) % MOD
    if C[pos] == 'b':
        dp[pos][1] = val1
        dp[pos][2] = (val2 - val1 + MOD) % MOD

dfs(0)
print(dp[0][2])