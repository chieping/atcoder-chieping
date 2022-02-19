from collections import defaultdict
N = int(input())
F = defaultdict(int)

i = 2
while i*i <= N:
    d, r = divmod(N, i)
    if r == 0:
        F[i] += 1
        N = d
    else:
        i += 1
F[N] += 1

ans = 0
for k, v in F.items():
    if k == 1:
        continue
    i = 1
    while v >= i:
        ans += 1
        v -= i
        i += 1
print(ans)