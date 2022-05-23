import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M, K = map(int, input().split())
ans = [0] * N
parent = [-1] * N

def unite(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[a] += parent[b]
    parent[b] = a

def find(a):
    p = parent[a]
    if p < 0:
        return a
    b = find(p)
    parent[a] = b
    return b

def same(a, b):
    return find(a) == find(b)

def size(a):
    return -parent[find(a)]

friend = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    friend[a].append(b)
    friend[b].append(a)
    unite(a, b)

block = [[] for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    block[a].append(b)
    block[b].append(a)
    # 友達候補かつブロック関係であれば予め-1する
    if same(a, b):
        ans[a] -= 1
        ans[b] -= 1

for i in range(N):
    ans[i] += size(i) - 1 - len(friend[i])

print(*ans)