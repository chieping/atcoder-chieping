import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
V = [0] * N
W = [0] * N
for i in range(N):
    V[i], W[i] = map(int, input().split())
INF = 10**20

def wdp():
    dp = {0:0}
    for v, w in zip(V, W):
        nxt = dp.copy()
        for key, val in dp.items():
            if key + w <= Q:
                if key+w in dp:
                    nxt[key+w] = max(dp[key+w], val+v)
                else:
                    nxt[key+w] = val + v
        dp = nxt

    print(max(dp.values()))

def vdp():
    dp = [INF] * (1000*N+1)
    dp[0] = 0
    for v, w in zip(V, W):
        nxt = dp.copy()
        for i in range(1000*N+1):
            if i - v >= 0:
                nxt[i] = min(nxt[i], dp[i-v]+w)
        dp = nxt
    for i in range(1000*N, -1, -1):
        if dp[i] <= Q:
            print(i)
            exit()

if N <= 30 or max(W) <= 1000:
    wdp()
else:
    vdp()
