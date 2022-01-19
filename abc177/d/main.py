import sys
readline = sys.stdin.readline
N, M = map(int, readline().split())
parents = [-1] * (N+1)

def unite(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[a] += parents[b]
        parents[b] = a

def find(a):
    p = parents[a]
    if p < 0:
        return a
    else:
        pp = find(p)
        parents[a] = pp
        return pp

for _ in range(M):
    a, b = map(int, readline().split())
    unite(a, b)

print(-min(parents))
