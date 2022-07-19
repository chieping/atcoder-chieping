import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, Q = map(int, input().split())
X = list(map(int, input().split()))
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append(b)
    edge[b].append(a)
V = []
K = []
for _ in range(Q):
    v, k = map(int, input().split())
    v -= 1
    k -= 1
    V.append(v)
    K.append(k)

M = [[] for _ in range(N)]

def dfs(v, p = -1):
    M[v].append(X[v])
    for u in edge[v]:
        if u == p: continue
        dfs(u, v)
        M[v] += M[u]
        M[v].sort(reverse=True)
        M[v] = M[v][:20]

dfs(0)

for v, k in zip(V, K):
    print(M[v][k])
