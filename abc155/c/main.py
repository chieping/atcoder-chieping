from collections import defaultdict
import sys
readline = sys.stdin.readline
N = int(readline())
C = defaultdict(int)
max_ = 0
for _ in range(N):
    s = readline()[:-1]
    C[s] += 1
    max_ = max(max_, C[s])
print(*sorted(k for k, v in C.items() if v == max_), sep='\n')