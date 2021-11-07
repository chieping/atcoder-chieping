import sys
sys.setrecursionlimit(10**6)
N = int(input())

T = []
K = []
A = []
mastered = [False] * N
for i in range(N):
    TKA = list(map(int, input().split()))
    T.append(TKA[0])
    K.append(TKA[1])
    A.append(list(map(lambda x: x-1, TKA[2:])))

def master(n):
    if len(A[n]) == 0:
        nn = 0
        if not mastered[n]:
            nn = T[n]
            mastered[n] = True
        return nn
    else:
        d = A[n].pop()
        dn = master(d)
        return dn + master(n)

print(master(N-1))
