MOD = 2**20
Q = int(input())
A = [-1] * MOD
P = [-1] * MOD

def find(x):
    # print('x:', x)
    if P[x] < 0:
        return x
    else:
        P[x] = find(P[x])
        return P[x]

def unite(x, y):
    # print('x:', x, 'y:', y)
    x = find(x)
    y = find(y)
    if x == y:
        return
    P[y] += P[x]
    P[x] = y


for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        if A[x % MOD] == -1:
            h = x%MOD
        else:
            h = find(x%MOD)
        A[h] = x
        unite(h, (h+1)%MOD)
    elif t == 2:
        print(A[x % MOD])
