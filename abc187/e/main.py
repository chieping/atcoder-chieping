import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
A = [0]
B = [0]
edges = [[] for _ in range(N+1)]
depth = [-1] * (N+1)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    edges[a].append(b)
    edges[b].append(a)

def depthDFS(a, d):
    depth[a] = d
    for edge in edges[a]:
        if depth[edge] == -1:
            depthDFS(edge, d+1)

def imosDFS(a, now):
    now += dp[a]
    dp[a] = now
    for edge in edges[a]:
        if depth[edge] > depth[a]:
            imosDFS(edge, now)

depthDFS(1, 0)

dp = [0] * (N+1)
Q = int(sys.stdin.readline())
for _ in range(Q):
    t, e, x = map(int, sys.stdin.readline().split())
    if t == 1:
        va = A[e]
        vb = B[e]
    elif t == 2:
        va = B[e]
        vb = A[e]
    
    if depth[va] < depth[vb]:
        dp[1] += x
        dp[vb] -= x
    else:
        dp[va] += x

imosDFS(1, 0)

print(*dp[1:], sep="\n")
