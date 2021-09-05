from collections import deque
import heapq

Q = int(input())

# deque
A1 = deque()
# 優先度付きキュー
A2 = []

for _ in range(Q):
    q = tuple(map(int, input().split()))

    if q[0] == 1:
        A1.append(q[1])
    elif q[0] == 2:
        if len(A2) != 0:
            print(heapq.heappop(A2))
        else:
            print(A1.popleft())
            
    elif q[0] == 3:
        while len(A1) > 0:
            heapq.heappush(A2, A1.pop())
