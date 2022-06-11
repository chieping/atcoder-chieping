from bisect import bisect_left
from itertools import accumulate
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
cum = [0] + list(accumulate(A))
X = [int(input()) for _ in range(Q)]

for x in X:
    i = bisect_left(A, x)
    ans = 0
    ans += (cum[-1] - cum[i]) - (x * (N-i))
    ans += abs(cum[i] - (x * i))
    print(ans)
