import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))

if not set(A) == set(B):
    print('No')
    exit()

# 同じ数値を偶奇が異なる順番で持っていればYes
if len(set([A[i] for i in range(0, N, 2)]).intersection(set([A[i] for i in range(1, N, 2)]))):
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
