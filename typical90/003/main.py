# N頂点n-1辺の連結なグラフ→木構造、閉路なし
# 辺を一本追加すると閉路が一つだけ出現し、長さは（u→vの単純パスの長さ）+1である
from collections import deque

N = int(input())
edges = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

def bfs(start):
    dist = [False] * N
    dist[start] = (0, 0)
    Q = deque()
    Q.append(start)
    while len(Q) > 0:
        v = Q.pop()
        for i in edges[v]:
            if dist[i] == False:
                dist[i] = (dist[v][0] + 1, i)
                Q.append(i)
    return dist

# 頂点1から各頂点までの最短距離を求める
D0 = bfs(0)

# 最も最短距離が大きかった頂点をuとして、頂点uからの最短距離を求める。
# そのときに出現した最短距離最大値がE(木の直径)の値である
u = max(D0)[1]
DM = bfs(u)

ans = max(DM)[0] + 1
print(ans)
