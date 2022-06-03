import sys
sys.setrecursionlimit(10**6)
MOD = 998244353
N = int(input())
F = [0] + list(map(int, input().split()))

parent = [-1] * (N+1)

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if parent[x] > parent[y]:
        x, y = y, x
    parent[x] += parent[y]
    parent[y] = x
    return True

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

for i in range(1, N+1):
    unite(i, F[i])

cycle_cnt = sum(True for p in parent[1:] if p < 0)

print(pow(2, cycle_cnt, MOD)-1)
