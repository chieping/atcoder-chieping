from collections import defaultdict
N, Q = map(int, input().split())
X, Y, Z, W = [], [], [], []
MOD = 10**9+7
for _ in range(Q):
    x, y, z, w = map(int, input().split())
    X.append(x-1)
    Y.append(y-1)
    Z.append(z-1)
    W.append(w)

cnt = defaultdict(int)

for bit in range(1 << N):
    ans = 0
    for x, y, z in zip(X, Y, Z):
        or_result = (((bit >> x) % 2) |
                     ((bit >> y) % 2) |
                     ((bit >> z) % 2))
        ans *= 2
        ans += or_result
    cnt[ans] += 1

res = 1
for i in range(60):
    ans = 0
    for w in W:
        ans *= 2
        ans += (w >> i) % 2
    res *= cnt[ans]
    res %= MOD
print(res)