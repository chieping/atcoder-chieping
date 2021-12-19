N, W = map(int, input().split())
INF = 10**18
dp = [[0] * N for i in range(N)]

ws = [0]
vs = [0]

for i in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

# value[品物iまで選んだとき][価値] = その価値における重さの最小
value = [[INF] * 100_001 for i in range(N+1)]
value[0][0] = 0
for i in range(1, N+1):
    for j in range(100_001):
        if j - vs[i] >= 0:
            value[i][j] = min(value[i-1][j], value[i-1][j-vs[i]] + ws[i])
        else:
            value[i][j] = value[i-1][j]

ans = 100000
while(value[N][ans] > W):
    ans -= 1

print(ans)
