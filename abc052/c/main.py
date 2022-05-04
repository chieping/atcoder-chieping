# 解説AC
from collections import Counter
N = int(input())
MOD = 10**9+7

fact = []
for n in range(1, N+1):
    i = 2
    while i*i <= n:
        d, r = divmod(n, i)
        if r == 0:
            fact.append(i)
            n = d
        else:
            i += 1
    fact.append(n)

ans = 1
for key, cnt in Counter(fact).items():
    if key == 1: continue
    ans *= cnt+1
    ans %= MOD
print(ans)
