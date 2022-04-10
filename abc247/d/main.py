from collections import deque
import sys
input = sys.stdin.readline

que = deque()

Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        x, c = q[1:]
        que.append((x, c))
    else:
        c = q[1]
        Sum = 0
        while c > 0:
            X, C = que.popleft()
            if c < C:
                nc = C-c
                que.appendleft((X, nc))
                Sum += X*c
                c = 0
            else:
                c -= C
                Sum += X*C
        print(Sum)

