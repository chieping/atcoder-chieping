import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))
setA = set(A)
if not setA == set(B):
    print('No')
    exit()

# 同じ数値を持っていればYes
if len(setA) < N:
    print('Yes')
    exit()

for i in range(N-2):
    b = B[i]
    aind = A.index(b)
    if i != aind:
        A[i], A[i+1:aind+1] = A[aind], A[i:aind]

    # 偶奇が異なるときはSwapが発生する
    if i % 2 ^ aind % 2:
        A[i+1], A[i+2] = A[i+2], A[i+1]

if A[-2] == B[-2] and A[-1] == B[-1]:
    print('Yes')
else:
    print('No')
