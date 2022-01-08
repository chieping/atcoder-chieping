from bisect import bisect_left
from sys import stdin
X = int(stdin.readline())

A = list(range(10))

for first in range(1, 10):
    for d in range(-9, 9):
        dg = first
        s = [dg]
        for i in range(18):
            dg += d
            if 0 <= dg <= 9:
                s.append(dg)
                A.append(int(''.join(map(str, s))))
            else:
                break

A.sort()
idx = bisect_left(A, X)
print(A[idx])

