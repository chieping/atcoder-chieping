from collections import deque
import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
Q = deque()
deleted_cnt = 0
current = -1
seq = 0

for i in range(N):
    a = A[i]
    Q.append(a)
    if current == a:
        seq += 1
    else:
        current = a
        seq = 1
    if current == seq:
        for _ in range(a):
            Q.pop()
        deleted_cnt += a
        l = len(Q)
        if l > 0:
            current = Q[-1]
            seq = 1
            i = -2
            while -i <= l and Q[i] == current:
                seq += 1
                i -= 1
        else:
            current = -1
            seq = 0
    print(len(Q))

