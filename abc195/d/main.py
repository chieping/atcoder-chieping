N, M, Q = map(int, input().split())
VW = []
for i in range(N):
    w, v = map(int, input().split())
    VW.append((v, w))
X = list(map(int, input().split()))
VW.sort(reverse=True)

for _ in range(Q):
    l, r = map(int, input().split())
    X2 = sorted(X[:l-1] + X[r:])
    ans = 0

    for v, w in VW:
        for i in range(len(X2)):
            if w <= X2[i]:
                ans += v
                X2.pop(i)
                break
    print(ans)
