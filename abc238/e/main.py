import sys
readline = sys.stdin.readline
N, Q = map(int, readline().split())

parents = [-1] * (N+1)

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parents[a] += parents[b]
    parents[b] = a

def find(a):
    if parents[a] < 0:
        return a
    else:
        parents[a] = find(parents[a])
        return parents[a]

for _ in range(Q):
    l, r = map(int, readline().split())
    l -= 1
    union(l, r)

if find(0) == find(N):
    print('Yes')
else:
    print('No')
