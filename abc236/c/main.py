from collections import Counter
import sys
readline = sys.stdin.readline
N, M = map(int, readline().split())
S = readline()[:-1].split()
T = readline()[:-1].split()
C = Counter(S + T)
for s in S:
    if C[s] == 2:
        print('Yes')
    else:
        print('No')