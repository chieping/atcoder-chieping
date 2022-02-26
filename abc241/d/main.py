import sys
from sortedcontainers import SortedList
readline = sys.stdin.readline
Q = int(readline())
A = SortedList()

for _ in range(Q):
    q = list(map(int, readline().split()))
    if q[0] == 1:
        x = q[1]
        A.add(x)
    elif q[0] == 2:
        x, k = q[1:]
        idx = A.bisect_right(x)
        if idx < k:
            print(-1)
        else:
            print(A[idx-k])
    else:
        x, k = q[1:]
        idx = A.bisect_left(x)
        if idx + k - 1 >= len(A):
            print(-1)
        else:
            print(A[idx+k-1])
