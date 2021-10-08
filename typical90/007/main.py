from bisect import bisect_left
from sys import stdin
N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
A.sort()
Q = int(stdin.readline())
for i in range(Q):
    b = int(stdin.readline())
    l = bisect_left(A, b)
    if l == N:
        r = l
    else:
        r = l+1
    print(min(abs(A[l-1] - b), abs(A[r-1] - b)))
