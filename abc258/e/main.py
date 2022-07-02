import sys
input = sys.stdin.readline
N, Q, X = map(int, input().split())
W = list(map(int, input().split()))

loop = [(0, 0)] * N
A = []
a = 0
cnt = 0
i = 0
while True:
    a += W[i]
    cnt += 1
    if a >= X:
        if loop[i][0] == 2:
            # ループ検知
            LenS = loop[i][1]+1
            LenE = len(A)
            break
        loop[i] = (loop[i][0] + 1, len(A))
        A.append(cnt)
        a = 0
        cnt = 0
    i = (i+1)%N

# print(LenS, LenE)
loopLen = LenE - LenS + 1
beforeLoop = LenS-1
# print(A)
for _ in range(Q):
    k = int(input())
    if k <= beforeLoop:
        print(A[k-1])
    else:
        kk = ((k-beforeLoop-1) % loopLen)
        k = beforeLoop + kk
        print(A[k])
