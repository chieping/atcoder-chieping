from bisect import bisect_left, bisect_right
from itertools import accumulate
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ACC = list(accumulate(A))
X = [int(input()) for _ in range(Q)]

for x in X:
    i = bisect_left(A, x)
    ans = 0
    if i < N:
        if i == 0:
            acc1 = 0
        else:
            acc1 = ACC[i-1]
        ans += (ACC[-1] - acc1) - (x * (N-i))
    if i > 0:
        ans += abs(ACC[i-1] - (x * i))
    print(ans)
    
    

