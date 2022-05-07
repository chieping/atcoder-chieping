# 強連結成分 (SCC, Strongly Connected Component) 分解
# 有向グラフにおいて、互いに行き来が可能な頂点の集合に分解する
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
G = [[] for _ in range(N)]
H = [[] for _ in range(N)]
A = []
B = []
I = []
used = [False] * N
cnts = 0
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    A.append(a)
    B.append(b)
    G[a].append(b)
    H[b].append(a)

def dfs(pos):
    # 1回目のDFS
    # 帰りがけの順を記録する
    # これは強連結成分を除いた大きい順のトポロジカルソートになっている
    used[pos] = True
    for i in G[pos]:
        if used[i] == False:
            dfs(i)
    I.append(pos)

def dfs2(pos):
    # 2回目のDFS
    # 元のグラフの辺を逆辺に置き換えたものに対して行う。
    # 1回目で採番した帰りがけの遅い順にDFSする。
    # 逆辺にすることで、自分より若い強連結成分以外の頂点
    # に行くことができないが、強連結成分同士には行ける。
    # これで一回のDFSで行ける頂点集合が強連結成分となる。
    global cnts
    used[pos] = True
    cnts += 1
    for i in H[pos]:
        if used[i] == False:
            dfs2(i)

for i in range(N):
    if used[i] == False:
        dfs(i)

ans = 0
used = [False] * N
for i in I[::-1]:
    if used[i]:
        continue
    cnts = 0
    dfs2(i)
    ans += cnts * (cnts-1) // 2

print(ans)