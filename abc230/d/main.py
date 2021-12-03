from collections import Counter

N, D = map(int, input().split())

imos = Counter()
# imos = [0] * (N+2)




for i in range(N):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r] -= 1

ans = 0
A = 0

imos.sort()
i = 0
for k, v in imos.items():
    if A == 0 and v > 0:
        i = k-1
    A += v
    if A == 0 and v < 0:
        ans += k - i
        i = k
    


# for i in range(1, 10**9):
#     A += imos[i]
#     if A > 0:
#         ans += 1

print(ans)


