from pprint import pprint
import sys
readline = sys.stdin.readline
N, Q = map(int, readline().split())

A = [0]*(N+1)

for _ in range(Q):
    l, r = map(int, readline().split())
    l -= 1
    A[l] += 1
    A[r] -= 1

# print(A)
for i in range(1, N):
    A[i] += A[i-1]

A = A[:N]
# print(A)

if min(A) == 0:
    print('No')
else:
    print('Yes')
