from collections import Counter, OrderedDict

N, D = map(int, input().split())

imos = OrderedDict()
# imos = [0] * (N+2)




for i in range(N):
    l, r = map(int, input().split())
    if not l in imos:
        imos[l] = 0
    if not r in imos:
        imos[r] = 0
    imos[l] += 1
    imos[r] -= 1

ans = 0
A = 0

i = 0
for k, v in sorted(imos.items()):
    if A == 0 and v > 0:
        i = k
    A += v
    if A == 0 and v < 0:
        ans += k - i + 1
        i = k
    


# for i in range(1, 10**9):
#     A += imos[i]
#     if A > 0:
#         ans += 1

print(ans)


