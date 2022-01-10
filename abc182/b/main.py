from collections import defaultdict
from sys import stdin
N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
M = defaultdict(int)

for a in A:
    i = 2
    factors = set()
    while i*i <= a:
        if a % i == 0:
            factors.add(i)
            a //= i
        else:
            i += 1
    factors.add(a)
    for f in factors:
        M[f] += 1

print(max(M.items(), key=lambda item: item[1])[0])

