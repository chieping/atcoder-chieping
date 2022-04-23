from itertools import product
import sys
from typing import Counter
input = sys.stdin.readline
N, K = map(int, input().split())
S = [list(input()[:-1]) for _ in range(N)]
ans = 0
for s in range(1<<N):
    C = Counter()
    for i in range(N):
        if s>>i&1:
            C.update(S[i])
    ans = max(ans, sum(cnt == K for cnt in C.values()))
print(ans)
