import array
from bisect import bisect_left, insort_left

L, Q = map(int, input().split())
K = array.array('i', [0, L])

for _ in range(Q):
    c, x = map(int, input().split())

    if c == 1:
        insort_left(K, x)
    else:
        j = bisect_left(K, x)
        print(K[j] - K[j-1])
