import sys
input = sys.stdin.readline
INF = 10**18
N, M = map(int, input().split())
es = []
for _ in range(M):
    a, b, c = map(int, input().split())
    es.append((a-1, b-1, c))

d = [[INF] * N for _ in range(N)]

# ワーシャルフロイドで最短距離を求める
for a, b, c in es:
    d[a][b] = c
    d[b][a] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

# 残す条件は以下
# - AiとBiの距離がCiであり、かつ
# - 削除前のグラフにおいて、AiとBiを結ぶ2本以上の辺を使った長さCiのパスが存在しない
# Ai,Bi間を、いずれかの点を経由して2本以上使った距離がCi以下であるパスがある場合、
# その辺を削除することができる
ans = 0
for a, b, c in es:
    unused = 0
    for i in range(N):
        if d[a][i] + d[i][b] <= c:
            unused = 1
    ans += unused
print(ans)