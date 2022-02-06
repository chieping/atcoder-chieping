import sys
readline = sys.stdin.readline
N, M = map(int, readline().split())
A = list(map(int, readline().split()))
vote = sum(A)
A.sort(reverse=True)
if A[M-1] * 4 * M >= vote:
    print('Yes')
else:
    print('No')