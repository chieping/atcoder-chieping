from collections import Counter
import sys
readline = sys.stdin.readline
N, M = map(int, readline().split())
A = Counter(list(map(int, readline().split())))
B = list(map(int, readline().split()))

for b in B:
    if A[b] > 0:
        A[b] -= 1
    else:
        print('No')
        exit()
print('Yes')