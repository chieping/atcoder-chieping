import sys
input = sys.stdin.readline
N = int(input())
Q = int(input())
events = []
for _ in range(Q):
    t, x, y, v = map(int, input().split())
    events.append([t, x-1, y-1, v])
parent = [-1] * N
Sum = [0] * (N-1)
potential = [0] * N
def unite(a, b):
    a = root(a)
    b = root(b)
    if a == b:
        return
    if a > b:
        a, b = b, a
    parent[a] += parent[b]
    parent[b] = a

def root(a):
    if parent[a] < 0:
        return a
    parent[a] = root(parent[a])
    return parent[a]

for t, x, _, v in events:
    if t == 0:
        Sum[x] = v

# A[0] == 0 とした場合の数列を前計算
for i in range(N-1):
    potential[i+1] = Sum[i] - potential[i]

for t, x, y, v in events:
    if t == 0:
        unite(x, y)
    else:
        if root(x) != root(y):
            print('Ambiguous')
        elif (x+y)%2 == 0:
            print(v+(potential[y]-potential[x]))
        else:
            print(potential[x]+potential[y]-v)