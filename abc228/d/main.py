MOD = 2**20
Q = int(input())
A = [-1] * (MOD)
parent = [i for i in range(MOD)]
for i in range(1, Q+1):
    t, x = map(int, input().split())
    if (t == 1):
        if A[x % MOD] == -1:
            h = x%MOD
        else:
            h = parent[x % MOD]
        A[h] = x
        parent[h] = parent[(h+1)%MOD]
    elif t == 2:
        print(A[x % MOD])
