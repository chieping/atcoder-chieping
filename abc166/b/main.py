from collections import Counter
from pprint import pprint
import sys
readline = sys.stdin.readline
N, K = map(int, readline().split())
C = Counter([])
for _ in range(K):
    readline()
    C.update(list(map(int, readline().split())))
ans = set(range(1, N+1)) - set(C.keys())
pprint(len(ans))