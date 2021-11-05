import math
ON = int(input())
N = ON
factors = []
i = 1
while i*i <= N:
    i += 1
    if N % i != 0:
        continue
    while N % i == 0:
        factors.append(i)
        N //= i
if N != 1 and ON != N:
    factors.append(N)

ans = 0
l = len(factors)
while l > 1:
    l = math.ceil(l/2)
    ans += 1
print(ans)
