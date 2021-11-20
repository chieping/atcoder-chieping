import heapq


MOD = 2**20
Q = int(input())
A = [-1] * (MOD)
for i in range(1, Q+1):
    t, x = map(int, input().split())
    if (t == 1):
        h = x
        
        while A[h % MOD] != -1:
            h += 1

        A[h % MOD] = x
    elif t == 2:
        print(A[x % MOD])
