from itertools import product
import sys
from typing import Counter
input = sys.stdin.readline

N, K = map(int, input().split())
S = [list(input()[:-1]) for _ in range(N)]
ans = 0

for bits in product([True, False], repeat=N):
    b = [i for b, i in zip(bits, range(N)) if b == True]
    sc = []
    for i in b:
        sc += S[i]
    c = Counter(sc)
    ret = 0
    for cnt in c.values():
        if cnt == K:
            ret += 1
    ans = max(ans, ret)
print(ans)
