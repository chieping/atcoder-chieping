from bisect import bisect_right
from itertools import accumulate
N, X = map(int, input().split())
L = list(map(int, input().split()))
M = list(accumulate(L))
ans = bisect_right(M, X) + 1
print(ans)