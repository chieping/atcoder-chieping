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
        rem = q[1]
        Sum = 0
        while rem > 0:
            X, C = que.popleft()
            if rem < C:
                nc = C-rem
                que.appendleft((X, nc))
                Sum += X*rem
                rem = 0
            else:
                rem -= C
                Sum += X*C
        print(Sum)