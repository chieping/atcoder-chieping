from collections import Counter
import sys
readline = sys.stdin.readline
N = int(readline())
S = [''.join(sorted(readline()[:-1])) for _ in range(N)]
C = Counter(S)
print(sum(C[s]-1 for s in S) // 2)
